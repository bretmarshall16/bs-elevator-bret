from Services import elevator_service


elevator = elevator_service.setup_elevator_service()
elevator_service.run_elevator(elevator)