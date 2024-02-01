/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";
import { browser } from "@web/core/browser/browser";

export class ApprovedButton extends ListController {
   setup() {
       this.orm = useService("orm");
       this.notification = useService("notification");
       var location = window.location;
       super.setup();
   }

   async getStateApproved() {
      const record_ids = await this.getSelectedResIds();
      await this.orm.call('device.assignment', 'check_rpc', [record_ids]);
      console.log(record_ids);
//      const reload = () => this.model.load();
      if('check_rpc'){
          this.notification.add("Status Updated", {
               type: "success",
          });
          self.location.reload(true)
      }
   }
}
registry.category("views").add("approved", {
        ...listView,
        Controller: ApprovedButton,
        buttonTemplate: "device_management.approved_state",
    });