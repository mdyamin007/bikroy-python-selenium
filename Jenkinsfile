node {
    try{
      def repoInformation = checkout scm
      def GIT_COMMIT_HASH = repoInformation.GIT_COMMIT


      def parallelTestConfiguration = [
        [
        '[Test GET Appointment 200 Ok]': 'Test/TestCase/test_GET_appointments/test_1_C321743_GET_Appointment_200_Ok',
        '[Test GET Appointment noteId null]': 'Test/TestCase/test_GET_appointments/test_2_C323936_GET_Appointment_noteId_null',
        '[Test GET Appointment StartEnd DateRange]': 'Test/TestCase/test_GET_appointments/test_4_C321746_GET_Appointment_StartEnd_DateRange',
        '[Test GET Appointment specific patientId ]': 'Test/TestCase/test_GET_appointments/test_5_C321747_GET_appointment_for_specific_patientId',
        '[Test GET Appointment 400 Bad Request]': 'Test/TestCase/test_GET_appointments/test_7_C321751_GET_appointment_400_Bad_Request',
        '[Test GET Appointment With Non Integrated DoctorId]': 'Test/TestCase/test_GET_appointments/test_8_C321754_GET_Appointment_With_Non_Integrated_DoctorId',
        '[Test GET Appointment Communication Error]': 'Test/TestCase/test_GET_appointments/test_9_C321755_GET_Appointment_Communication_Error',
        '[Test GET Appointment No Appointments Assigned For DoctorId]': 'Test/TestCase/test_GET_appointments/test_10_C321756_GET_Appointment_No_Appointments_Assigned_For_DoctorId',
        '[Test GET Appointment 401 UnAuthorized]': 'Test/TestCase/test_GET_appointments/test_11_C321758_GET_Appointment_401_UnAuthorized',
        '[Test GET Appointment 404 Not Found]': 'Test/TestCase/test_GET_appointments/test_13_C321760_GET_Appointment_404_Not_Found',
        '[Test GET Lab Result 200]': 'Test/TestCase/test_GET_lab_results/test_1_C323935_GET_Lab_Result_200',
        '[Test GET Lab Result 400]': 'Test/TestCase/test_GET_lab_results/test_2_C323938_GET_Lab_Result_400',
        '[Test GET Lab Result 401]': 'Test/TestCase/test_GET_lab_results/test_3_C323939_GET_Lab_Result_401',
        '[Test GET medications 200]': 'Test/TestCase/test_GET_medications/test_1_C323969_GET_medications_200',
        '[Test GET medications 400]': 'Test/TestCase/test_GET_medications/test_2_C323987_GET_medications_400',
        '[Test GET medications 401]': 'Test/TestCase/test_GET_medications/test_3_C323988_GET_medications_401',
        '[Test GET ping 200]': 'Test/TestCase/test_GET_ping/test_1_C323974_GET_ping_200',
        '[Test GET ping 400]': 'Test/TestCase/test_GET_ping/test_2_C323989_GET_ping_400',
        '[Test GET ping 401]': 'Test/TestCase/test_GET_ping/test_3_C324060_GET_ping_401',
        '[Test GET vitals 200 OK ]': 'Test/TestCase/test_GET_vitals/test_1_C323975_GET_vitals_200_OK',
        '[Test GET vitals 401 Unauthorized]': 'Test/TestCase/test_GET_vitals/test_2_C323976_GET_vitals_401_Unauthorized',
        '[Test GET vitals noteId was not found]': 'Test/TestCase/test_GET_vitals/test_3_C323977_GET_vitals_noteId_was_not_found',
        '[Test GET vitals 500]': 'Test/TestCase/test_GET_vitals/test_4_C323978_GET_vitals_500',
        '[Test POST appointment notes 200 OK]': 'Test/TestCase/test_POST_appointment_notes/test_1_C321826_POST_appointment_notes_200_OK',
        '[Test POST appointment notes non existent note Id]': 'Test/TestCase/test_POST_appointment_notes/test_2_C321877_POST_appointment_notes_non_existent_note_Id',
        '[Test POST appointment notes invalid integration id ]': 'Test/TestCase/test_POST_appointment_notes/test_3_C321878_POST_appointment_notes_invalid_integration_id',
        '[Test POST appointment notes NoteId_Created But Not Integrated]': 'Test/TestCase/test_POST_appointment_notes/test_4_C321879_POST_appointment_notes_NoteId_Created_But_Not_Integrated',
        '[Test POST appointment notes noteId with a deletion date]': 'Test/TestCase/test_POST_appointment_notes/test_5_C321880_POST_appointment_notes_noteId_with_a_deletion_date',
        '[Test POST appointment notes invalid ehrPatientId]': 'Test/Tese/test_POStCasT_appointment_notes/test_6_C321881_POST_appointment_notes_invalid_ehrPatientId',
        '[Test POST appointment notes invalid appointId]': 'Test/TestCase/test_POST_appointment_notes/test_7_C321882_POST_appointment_notes_invalid_appointId',
        '[Test POST physicians sync 200 ]': 'Test/TestCase/test_POST_physicians_sync/test_1_C321883_POST_physicians_sync_200',
        '[Test POST physicians sync 200 noSiteId]': 'Test/TestCase/test_POST_physicians_sync/test_2_C321884_POST_physicians_sync_200_noSiteId',
        '[Test POST physicians sync 200 data retrieval error]': 'Test/TestCase/test_POST_physicians_sync/test_3_C321885_POST_physicians_sync_200_data_retrieval_error',
        '[Test POST physicians sync 400]': 'Test/TestCase/test_POST_physicians_sync/test_4_C323985_POST_physicians_sync_400',
        '[Test POST physicians sync 401]': 'Test/TestCase/test_POST_physicians_sync/test_5_C323986_POST_physicians_sync_401',
        '[Test POST physicians sync no service]': 'Test/TestCase/test_POST_physicians_sync/test_6_C324059_POST_physicians_sync_no_service',
        '[Test ehr GetAppointment noteId patientInfo crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_0_ehr_GetAppointment_noteId_patientInfo_crosscheck',
        '[Test lk ehr GetAppointment crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_1_lk_ehr_GetAppointment_crosscheck',
        '[Test lk ehr GetMedications crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_2_lk_ehr_GetMedications_crosscheck',
        '[Test lk ehr GetAllergies crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_3_lk_ehr_GetAllergies_crosscheck',
        '[Test lk ehr GetImmunizations crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_4_lk_ehr_GetImmunizations_crosscheck',
        '[Test lk ehr GetLabResults crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_5_lk_ehr_GetLabResults_crosscheck',
        '[Test lk ehr SiteServiceKey crosscheck]': 'Test/TestCase/test_Lk_crosscheck/test_6_lk_ehr_SiteServiceKey_crosscheck'
        ]
      ]

      def stepList = prepareBuildStages(parallelTestConfiguration)

      for (def groupOfSteps in stepList) {
        parallel groupOfSteps
      }

    } catch(error) {
      echo "The following error occurred: ${error}"
      throw error
    } finally {
      allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'target/allure-results']]
      ])
    }
}


def prepareBuildStages(List<Map<String,String>> parallelTestConfiguration) {
  def stepList = []

  println('Preparing builds...')

  for (def parallelConfig in  parallelTestConfiguration) {
    def parallelSteps = prepareParallelSteps(parallelConfig)
    stepList.add(parallelSteps)
  }

  println(stepList)
  println('Finished preparing builds!')

  return stepList
}


def prepareParallelSteps(Map<String, String> parallelStepsConfig) {
  def parallelSteps = [:]
  for (def key in parallelStepsConfig.keySet()) {
    parallelSteps.put(key, prepareOneBuildStage(key, parallelStepsConfig[key]))
  }
  return parallelSteps
}

def prepareOneBuildStage(String name, String file) {
  return {
    stage("Test: ${name}") {
      println("Test: ${name}")
        withCredentials([
            string(credentialsId: 'pwd_jz_su', variable: 'pwd_jz_su'),
            string(credentialsId: 'db_pwd_aws', variable: 'db_pwd_aws'),
            string(credentialsId: 'selenium_grid_16ram', variable: 'selenium_grid_16ram'),
            ]) {
              // Tests go here
              sh """
                python3 -m pytest ${file}.py --alluredir=${WORKSPACE}/allure-results
              """
          }
    }
  }
}