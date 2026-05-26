# Brusnika LMS — Frappe / ERPNext Integration

Connect your Frappe or ERPNext instance to [Brusnika.LMS](https://brusnika-lms.com/) — a cloud Learning Management System built for teams.

## What this app does

After installing, a **Brusnika LMS Settings** page appears in your Frappe desk. It stores your LMS URL and shows step-by-step instructions for completing the connection from the LMS side.

Once connected, Brusnika.LMS can:

- **Sync employees / users** — all active Frappe users (or ERPNext Employees) are available as LMS learners
- **Sync departments** — Frappe Departments are imported as LMS groups for targeted course assignments
- **Create tasks** — LMS-assigned deadlines and to-dos appear as Frappe ToDo records
- **Send notifications** — course reminders are delivered as low-priority Frappe ToDo notifications

## Requirements

- Frappe v14, v15, or v16
- An active [Brusnika.LMS](https://brusnika-lms.com/) subscription

## Setup

1. Install this app via Frappe bench:
   ```
   bench get-app brusnika_lms https://github.com/BrusnikaLMS/brusnika_lms_frappe
   bench --site yoursite.local install-app brusnika_lms
   ```
2. Open **Brusnika LMS Settings** from the Frappe desk.
3. Save your LMS URL and follow the on-screen instructions to connect from the LMS admin panel.

## Support

- Website: [https://brusnika-lms.com/](https://brusnika-lms.com/)
- Email: [info@brusnika-solutions.com](mailto:info@brusnika-solutions.com)

## License

MIT — see [LICENSE.txt](LICENSE.txt)
