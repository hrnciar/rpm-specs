Name:          standard-test-roles
Version:       4.9
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
* Fri Oct 02 2020 Andrei Stepanov <astepano@redhat.com> - 4.9-1
- Build with the latest merged PRs.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Andrei Stepanov <astepano@redhat.com> - 4.8-1
- Build with the latest merged PRs.
