##Fix git error : object file is empty

[Reference](http://stackoverflow.com/a/12371337)

* Backup:  `sudo cp -a .git .git-old`
* Find empty files: `sudo git fsck –full`

```
error: object file .git/objects/33/b2710a3f7a6e5cb8201d748056bf79f0348812 is empty
error: object file .git/objects/33/b2710a3f7a6e5cb8201d748056bf79f0348812 is empty
fatal: loose object 33b2710a3f7a6e5cb8201d748056bf79f0348812 (stored in .git/objects/33/b2710a3f7a6e5cb8201d748056bf79f0348812) is corrupt
```

* Delete empty file `sudo rm .git/objects/33/b2710a3f7a6e5cb8201d748056bf79f0348812` then `sudo git fsck –full`until empty files are removed. You will get this message.

```odoo@odoo-VirtualBox:/odoo/odoo-fhir$ sudo git fsck --fullChecking object directories: 100% (256/256), done.
Checking objects: 100% (5955/5955), done.
error: HEAD: invalid sha1 pointer 767b35323f8b43bfaa6f21b4a562473e51561b57
error: refs/heads/master: invalid sha1 pointer 767b35323f8b43bfaa6f21b4a562473e51561b57
error: refs/remotes/origin/HEAD: invalid sha1 pointer 767b35323f8b43bfaa6f21b4a562473e51561b57
error: refs/remotes/origin/master: invalid sha1 pointer 767b35323f8b43bfaa6f21b4a562473e51561b57
notice: No default references
error: bcbf403bec727e58c242f2f9401455077431b596: invalid sha1 pointer in cache-tree
error: fe634835abf46066d4d5a3d4cc76756ab5e7c454: invalid sha1 pointer in cache-tree
error: 61faab3c813b073c11a3c72ec024232aca9551d9: invalid sha1 pointer in cache-tree
error: e64cd7d613b0f87e2b7c15cfc295f1b75a08a10c: invalid sha1 pointer in cache-tree
error: 33b2710a3f7a6e5cb8201d748056bf79f0348812: invalid sha1 pointer in cache-tree
missing blob d08270254e3592fbf8e871f8b7d4cb8e644a6c67
missing blob 456cf917fac2d0bf37309a9c6a73923b25d9b841
missing blob fcf1c05a36ba9421192df898344b3ef5cde19549
missing blob 76362a2490e5028e96ecc098eabeed478fa7ccaf
missing blob 92b8f10c9fbe8147f3cbb271a280585b0459a38b
missing blob 783b176c7c3c2d825c29794ae629fe115ad599eb
```
* Try `git reflog`
```fatal: bad object HEAD```

* Get last 2 lines of the reflog `tail -n 2 .git/logs/refs/heads/master`

```16326ea08ee42069d8fd3d0af360618f0bf73c28 b3b21a92bed2988eaf089d71d3f9643841291890 Luigi Sison <lsison@moxylus.com> 1483544046 -0800	commit: changes```

* `sudo git show b3b21a92bed2988eaf089d71d3f9643841291890`

* Point HEADv`sudo git update-ref HEAD b3b21a92bed2988eaf089d71d3f9643841291890`

* Kill the index file and reset the repo
`sudo rm .git/index`
`sudo git reset`

* Show changes `sudo git fsck –full`

```
M	addons/hc_allergy_intolerance/__openerp__.py
D	addons/hc_allergy_intolerance/data/hc.vs.route.code.csv
M	addons/hc_allergy_intolerance/models/hc_res_allergy_intolerance.py
D	addons/hc_allergy_intolerance/views/hc_route_code_views.xml
M	addons/hc_base/__openerp__.py
M	addons/hc_base/security/ir.model.access.csv
M	addons/hc_base/views/hc_participation_type_views.xml
M	addons/hc_base/views/views.xml
M	addons/hc_care_team/models/hc_res_care_team.py
M	addons/hc_device/models/hc_res_device.py
M	addons/hc_family_member_history/security/ir.model.access.csv
M	addons/hc_group/models/hc_res_group.py
M	addons/hc_group/views/hc_res_group_views.xml
M	addons/hc_medication/models/hc_res_medication.py
M	addons/hc_medication_administration/models/hc_res_medication_administration.py
M	addons/hc_medication_administration/security/ir.model.access.csv
M	addons/hc_medication_dispense/models/hc_res_medication_dispense.py
M	addons/hc_medication_statement/models/hc_res_medication_statement.py
M	addons/hc_medication_statement/security/ir.model.access.csv
M	addons/hc_patient/models/hc_res_patient.py
M	addons/hc_procedure_request/models/hc_res_procedure_request.py
M	addons/hc_procedure_request/security/ir.model.access.csv
M	addons/hc_referral_request/models/hc_res_referral_request.py
```
* Try to push changes to repo `sudo git add .` `sudo git commit -m "changes" -a` `sudo git push origin master`

