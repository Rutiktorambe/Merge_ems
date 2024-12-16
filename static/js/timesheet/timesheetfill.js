{
  /* <script src="{{ url_for('static', filename='js/timesheet/timesheetfill.js') }}"></script>; */
}

// ----------------------------------------------------UpdateCategories------------------------------------

async function updateCategories() {
  const allocationType = document.getElementById("allocationType").value;
  const category1 = document.getElementById("category1");
  const category2 = document.getElementById("category2");
  const category3 = document.getElementById("category3");
  const projectCode = document.getElementById("projectCode");

  category1.innerHTML = "<option value=''>Select</option>";
  category2.innerHTML = "<option value=''>Select</option>";
  category3.innerHTML = "";
  projectCode.value = "";

  if (allocationType === "billable") {
    const billableOptions = [
      "Pricing",
      "Capital",
      "Analytics",
      "Reserving",
      "CIO-UK",
      "HR",
    ];
    billableOptions.forEach((option) =>
      category1.options.add(new Option(option, option))
    );

    category1.onchange = async function () {
      const selectedCategory = category1.value;
      const response = await fetch(
        `/timesheet/get_projects/${selectedCategory}`
      );
      const projects = await response.json();

      category2.innerHTML = "<option value=''>Select Project</option>";

      if (projects.length > 0) {
        projects.forEach((project) => {
          const option = new Option(project.ProjectName, project.ProjectName);
          option.setAttribute("data-code", project.ProjectCode);
          category2.options.add(option);
        });

        category2.onchange = function () {
          const selectedOption = category2.options[category2.selectedIndex];
          const projectCodeValue = selectedOption.getAttribute("data-code");
          projectCode.value = projectCodeValue;

          category3.innerHTML = "";
          const thirdCategoryOptions = [
            "Planning",
            "Project Training",
            "Data Analysis",
            "Meeting",
            "Peer Review",
            "Report & Documentation",
          ];
          thirdCategoryOptions.forEach((option) =>
            category3.options.add(new Option(option, option))
          );
        };
      } else {
        category2.innerHTML = "<option value=''>No Projects Available</option>";
      }
    };
  } else if (allocationType === "non-billable") {
    const nonBillableOptions = {
      Admin: [
        { name: "Select", code: "" },
        { name: "Performance & Review & 1-2-1", code: "A100" },
        { name: "IT issue", code: "A200" },
        { name: "Team Meeting", code: "A300" },
        { name: "Marketing", code: "A400" },
        { name: "Recruitment & People", code: "A500" },
        { name: "Social Events", code: "A600" },
        { name: "Finance", code: "A700" },
        { name: "Other", code: "A800" },
      ],
      Training: [
        { name: "Select", code: "" },
        { name: "Internal", code: "" },
        { name: "External", code: "" },
        { name: "Self", code: "T300" },
        { name: "Other", code: "T600" },
      ],
    };

    for (let option in nonBillableOptions) {
      category1.options.add(new Option(option, option));
    }

    category1.onchange = function () {
      const selectedCategory = category1.value;
      category2.innerHTML = "";
      category3.innerHTML = "";
      projectCode.value = "";

      if (nonBillableOptions[selectedCategory]) {
        nonBillableOptions[selectedCategory].forEach((option) => {
          const opt = new Option(option.name, option.name);
          opt.setAttribute("data-code", option.code);
          category2.options.add(opt);
        });
      }

      category2.onchange = async function () {
        const selectedOption = category2.options[category2.selectedIndex];
        const selectedProjectCode = selectedOption.getAttribute("data-code");

        category3.innerHTML = "";
        projectCode.value = selectedProjectCode;

        if (
          selectedOption.value === "Internal" ||
          selectedOption.value === "External"
        ) {
          try {
            const Valueinput = selectedOption.value;
            const trainingInput = Valueinput.toLowerCase();

            const response = await fetch(
              `/timesheet/get_trainings/${trainingInput}`
            );
            const trainings = await response.json();

            if (trainings.length > 0) {
              trainings.forEach((training) => {
                const option = new Option(training.TName, training.TName);
                option.setAttribute("data-code", training.TID);
                category3.options.add(option);
              });

              category3.onchange = function () {
                const selectedTrainingOption =
                  category3.options[category3.selectedIndex];
                const trainingTID =
                  selectedTrainingOption.getAttribute("data-code");
                projectCode.value = trainingTID || "";
              };
            } else {
              category3.innerHTML =
                "<option value=''>No Trainings Available</option>";
            }
          } catch (error) {
            alert("Error in the backend to fetch the data", error);
            category3.innerHTML =
              "<option value=''>Error Loading Trainings</option>";
          }
        }
        if (selectedCategory === "Admin" && selectedProjectCode === "A800") {
          [
            "Other",
            "Vision_2016",
            "EMS",
            "YouRSAY",
            "Project_Planning_Document",
            "Vision_Data_Project",
            "Group_Internal_Audit",
            "Transfer_Pricing",
            "Project_butterfly",
            "Revenue_Management",
            "KPI_Research_Project",
            "ME_Pricing_Training",
            "Big_Upgrade",
            "Y2016_Graduate_Training_Mandatory",
            "Y2016_Graduate_Training_Mandatory",
          ].forEach((sub) => {
            category3.options.add(new Option(sub, sub));
          });

          category3.onchange = function () {
            const subCategory = category3.value;
            const subCodes = {
              Other: "A800",
              Vision_2016: "A801",
              EMS: "A802",
              YouRSAY: "A803",
              Project_Planning_Document: "A804",
              Vision_Data_Project: "A805",
              Group_Internal_Audit: "A806",
              Transfer_Pricing: "A807",
              Project_butterfly: "A808",
              Revenue_Management: "A809",
              KPI_Research_Project: "A810",
              ME_Pricing_Training: "A811",
              Big_Upgrade: "A812",
              Y2016_Graduate_Training_Mandatory: "A813",
              Y2016_Graduate_Training_Mandatory: "A814",
            };
            projectCode.value = subCodes[subCategory] || selectedProjectCode;
          };
        } else if (
          selectedCategory === "Training" &&
          selectedProjectCode === "T600"
        ) {
          [
            "Other",
            "Learning_Zone",
            "Vehicle_classification",
            "Exposure_based_Pricing",
            "Distribution_Fitting",
            "Reserving_John_Crooks",
            "Time_Series_Analysis",
            "Induction_Program",
          ].forEach((sub) => {
            category3.options.add(new Option(sub, sub));
          });

          category3.onchange = function () {
            const subCategory = category3.value;
            const subCodes = {
              Other: "T600",
              Learning_Zone: "T601",
              Vehicle_Classification: "T602",
              Exposure_based_Pricing: "T603",
              Distribution_Fitting: "T604",
              Reserving_John_Crooks: "T605",
              Time_Series_Analysis: "T606",
              Induction_Program: "T607",
            };
            projectCode.value = subCodes[subCategory] || selectedProjectCode;
          };
        }
      };
    };
  }
}

// ---------------------------------ValidateForm--------------------------------------------------
async function validateForm(event) {
  const allocationType = document.getElementById("allocationType").value;
  const selectedDates = document.querySelectorAll(
    "#dateDurations .ts-form-row"
  );
  const projectCode = document.getElementById("projectCode").value;
  const category1 = document.getElementById("category1").value;
  const category2 = document.getElementById("category2").value;

  if (event) event.preventDefault();

  if (!allocationType || allocationType === "required") {
    alert("Allocation Type is required.");
    return false;
  }

  if (selectedDates.length === 0) {
    alert("Please select at least one Date of Entry.");
    return false;
  }

  if (!projectCode) {
    alert(
      "Project Code is required. Please ensure valid categories are selected."
    );
    return false;
  }

  let fromDates = [];
  let toDates = [];

  if (allocationType === "billable") {
    try {
      const response = await fetch(`/timesheet/projectCode/${projectCode}`);

      const projects = await response.json();

      if (projects.length === 0) {
        alert("Invalid Project Code or no projects found.");
        return false;
      }

      const project = projects[0];
      fromDates = [new Date(project.FromDate)];
      toDates = [new Date(project.ToDate)];
    } catch (error) {
      alert("Failed to validate Project Code. Please try again.");
      return false;
    }
  }

  for (const row of selectedDates) {
    const dateLabel = row.querySelector("label").innerText.split(" - ")[0];
    const date = new Date(dateLabel);

    if (
      allocationType === "billable" &&
      (date < fromDates[0] || date > toDates[0])
    ) {
      row.style.border = "2px solid red";
      alert(
        `The ${category2} with Project Code "${projectCode}" is not valid for "${dateLabel}". Date must be between ${fromDates[0].toDateString()} and ${toDates[0].toDateString()}.`
      );
      return false;
    } else {
      row.style.border = "";
    }

    const hoursField = row.querySelector(`select[name="hours_${dateLabel}"]`);
    const minutesField = row.querySelector(
      `select[name="minutes_${dateLabel}"]`
    );
    const hours = parseInt(hoursField?.value || "0", 10);
    const minutes = parseInt(minutesField?.value || "0", 10);

    if (isNaN(hours) || isNaN(minutes) || (hours === 0 && minutes === 0)) {
      row.style.border = "2px solid red";
      showNotification(
        `Please log hours and/or minutes for the selected date: ${dateLabel}`
      );
      return false;
    }

    let previoustime = 0;
    try {
      const formattedDate = date.toISOString().split("T")[0];
      const response = await fetch(`/timesheet/get_datetime/${formattedDate}`);
      // const response = await fetch(`/timesheet/get_datetime/${formattedDate}`, {
      //   headers: {
      //     "X-Requested-With": "XMLHttpRequest",
      //   },
      // });
      const timedata = await response.json();
      previoustime = parseFloat(Object.values(timedata)[0] || "0");
    } catch (error) {
      console.error("Error fetching time data:", error);
    }

    const inputTime = parseFloat(hours + minutes / 60);
    const newTime = (inputTime + previoustime).toFixed(2);

    if (newTime > 24) {
      alert(
        `You are trying to fill entries of ${newTime} hours in a single 24-hour day.`
      );
      return false;
    }
  }

  if (!category1) {
    alert("Category 1 is required.");
    return false;
  }

  if (!category2) {
    alert("Category 2 is required.");
    return false;
  }

  document.getElementById("timesheetForm").submit();
  return true;
}

// -------------------------------------------FetchSummary-------------------------------------------------
function fetchSummary(dates) {
  fetch("/timesheet/history", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ dates: dates }),
  })
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document
        .getElementById("timesheetSummaryTable")
        .querySelector("tbody");
      tableBody.innerHTML = "";
      for (const [date, totalTime] of Object.entries(data)) {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${date}</td><td>${totalTime} hours</td>`;
        tableBody.appendChild(row);
      }
    })
    .catch((error) => console.error("Error fetching summary:", error));
}

function showNotification(message) {
  // Check if notification already exists
  let notification = document.getElementById("customNotification");
  if (!notification) {
    // Create the notification
    notification = document.createElement("div");
    notification.id = "customNotification";
    notification.style.position = "fixed";
    notification.style.top = "20px";
    notification.style.right = "20px";
    notification.style.backgroundColor = "#f44336"; // Red background
    notification.style.color = "white";
    notification.style.padding = "10px 20px";
    notification.style.borderRadius = "5px";
    notification.style.boxShadow = "0 2px 6px rgba(0, 0, 0, 0.3)";
    notification.style.fontSize = "16px";
    notification.style.zIndex = "1000";
    notification.style.opacity = "0";
    notification.style.transition = "opacity 0.5s ease";
    document.body.appendChild(notification);
  }

  // Update the message
  notification.textContent = message;

  // Show the notification
  notification.style.opacity = "1";

  // Hide after 3 seconds
  setTimeout(() => {
    notification.style.opacity = "0";
  }, 3000);
}
