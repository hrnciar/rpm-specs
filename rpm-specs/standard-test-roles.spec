Name:          standard-test-roles
Version:       4.7
Release:       1%{?dist}
Summary:       Standard Test Interface Ansible roles

License:       MIT
URL:           https://fedoraproject.org/wiki/Changes/InvokingTestsAnsible
Source0:       http://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: coreutils
Requires:      ansible fmf
# We want the real ssh for Ansible, otherwise it may fall back to paramiko
# which doesn't work in a whole lot of scenarios. Ref: PR1 for STR.
Requires:      openssh-clients
Requires:      standard-test-roles-inventory-qemu

%description
Shared Ansible roles to support the Standard Test Interface as described
at %{url}.

%package inventory-qemu
Summary:       Inventory provisioner for using plain qemu command
Requires:      qemu-system-x86
Requires:      genisoimage
Requires:      python3-fmf
%description inventory-qemu
Creates ansible inventory.  Implements provisioner for qemu where test subject
is vm image.

%package inventory-docker
Summary:       Inventory provisioner for using docker
Requires:      docker
%description inventory-docker
Creates ansible inventory.  Implements provisioner for docker where test
subject is docker containers.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/roles
cp -pr roles/* %{buildroot}%{_datadir}/ansible/roles/
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 scripts/merge-standard-inventory %{buildroot}/%{_bindir}/merge-standard-inventory
install -p -m 0755 scripts/str-filter-tests %{buildroot}/%{_bindir}/str-filter-tests
install -p -m 0755 scripts/qcow2-grow %{buildroot}/%{_bindir}/qcow2-grow
mkdir -p %{buildroot}%{_datadir}/ansible/inventory
cp -p inventory/* %{buildroot}%{_datadir}/ansible/inventory/

%files
%license LICENSE
%doc README.md
%config %{_datadir}/ansible/roles/*
%{_bindir}/merge-standard-inventory
%{_bindir}/str-filter-tests
%{_datadir}/ansible/inventory/standard-inventory-local
%{_datadir}/ansible/inventory/standard-inventory-rpm

%files inventory-qemu
%{_bindir}/qcow2-grow
%{_datadir}/ansible/inventory/standard-inventory-qcow2

%files inventory-docker
%{_datadir}/ansible/inventory/standard-inventory-docker

%changelog
* Mon Jun 08 2020 Andrei Stepanov <astepano@redhat.com> - 4.7-1
- Build with the latest merged PRs.

* Mon May 04 2020 Andrei Stepanov <astepano@redhat.com> - 4.6-2
- Remove patch. It was merged to upstream.

* Mon May 04 2020 Andrei Stepanov <astepano@redhat.com> - 4.6-1
- Build with the latest merged PRs.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Andrei Stepanov <astepano@redhat.com> - 4.5-3
- Add patch for beakerlib role.

* Mon Nov 04 2019 Andrei Stepanov <astepano@redhat.com> - 4.5-2
- Fix ansible requirements.

* Thu Oct 31 2019 Andrei Stepanov <astepano@redhat.com> - 4.5-1
- Build with the latest merged PRs.

* Wed Oct 09 2019 Andrei Stepanov <astepano@redhat.com> - 4.4-1
- Build with the latest merged PRs.

* Thu Aug 15 2019 Andrei Stepanov <astepano@redhat.com> - 4.3-1
- Build with the latest merged PRs.

* Tue Jul 16 2019 Andrei Stepanov <astepano@redhat.com> - 4.2-1
- Sync with upstream release 4.2

* Tue May 28 2019 Andrei Stepanov <astepano@redhat.com> - 4.1-1
- Sync with upstream release 4.1

* Wed May 15 2019 Andrei Stepanov <astepano@redhat.com> - 4.0-1
- Build with the latest merged PRs.

* Tue Mar 19 2019 Andrei Stepanov <astepano@redhat.com> - 3.2-1
- Build with the latest merged PRs.

* Thu Feb 14 2019 Andrei Stepanov <astepano@redhat.com> - 3.1-1
- Build with the latest merged PRs.

* Wed Jan 02 2019 Andrei Stepanov <astepano@redhat.com> - 3.0-1
- Build with the latest merged PRs.

* Thu Sep 20 2018 Andrei Stepanov <astepano@redhat.com> - 2.17-1
- Build with the latest merged PRs.

* Mon Sep 03 2018 Andrei Stepanov <astepano@redhat.com> - 2.16-1
- Build with the latest merged PRs.

* Mon Aug 20 2018 Andrei Stepanov <astepano@redhat.com> - 2.15-1
- Build with the latest merged PRs.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Andrei Stepanov <astepano@redhat.com> - 2.14-1
- Build with the latest merged PRs.

* Fri May 25 2018 Andrei Stepanov <astepano@redhat.com> - 2.13-2
- Build with the latest merged PRs.

* Wed May 23 2018 Andrei Stepanov <astepano@redhat.com> - 2.12-1
- Build with the latest merged PRs.

* Mon May 21 2018 Andrei Stepanov <astepano@redhat.com> - 2.11-1
- Build with the latest merged PRs.

* Mon Apr 23 2018 Andrei Stepanov <astepano@redhat.com> - 2.10-1
- Build with the latest merged PRs.

* Wed Mar 07 2018 Andrei Stepanov <astepano@redhat.com> - 2.9-1
- Build with the latest merged PRs.

* Tue Feb 13 2018 Andrei Stepanov <astepano@redhat.com> - 2.8-1
- Build with the latest merged PRs.

* Mon Feb 12 2018 Andrei Stepanov <astepano@redhat.com> - 2.7-2
- Fix changelog entry.

* Mon Feb 12 2018 Andrei Stepanov <astepano@redhat.com> - 2.7-1
- Build with the latest merged PRs.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Andrei Stepanov <astepano@redhat.com> - 2.6-2
- Build with the latest merged PRs.

* Wed Nov 15 2017 Andrei Stepanov <astepano@redhat.com> - 2.5-1
- Pkg build with the latest merged PRs.

* Thu Aug 17 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.4-1
- Sync with upstream release 2.4
- Bug fix in rhts role

* Wed Aug 09 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.3-1
- Sync with upstream release 2.3
- Adds merge-standard-inventory

* Fri Jul 28 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.1-1
- Sync with upstream release 2.1
- Add package dependencies for docker, genisoimage, and qemu-system-x86
  needed by dynamic inventory scripts

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.0-1
- Sync with upstream release 2.0.
- Add dynamic inventory scripts for qcow2, docker, rpm, and local

* Fri Jul 07 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.0-1
- Sync with upstream release 1.0.
- Rework beakerlib and cloud roles to work on Atomic Hosts
- Update standard-test-selector role for Atomic Host
- Update docker and rhts roles to be compatible with revised cloud and beakerlib roles

* Mon Jun 19 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.5-1
- Sync with upstream release 0.5.

* Mon Jun 05 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.4-1
- Sync with upstream release 0.4.

* Wed May 03 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.3-1
- Sync with upstream release 0.3.

* Tue May 02 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.2-2
- Updates based on review feedback.

* Thu Apr 27 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.2-1
- Sync with upstream release 0.2.

* Wed Apr 26 2017 Merlin Mathesius <mmathesi@redhat.com> - 0.1-1
- Initial packaging for Fedora.
