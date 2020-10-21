%global githash 79d751a


Name:		ansible-openstack-modules
Version:	0
Release:	20140912git%{githash}%{?dist}
Summary:	Unofficial Ansible modules for managing Openstack

License:	GPLv3
URL:		https://github.com/openstack-ansible/openstack-ansible-modules
# git clone https://github.com/openstack-ansible/openstack-ansible-modules.git
# cd openstack-ansible-modules
# git archive --format=tar %%{githash} | gzip > %%{name}-%%{githash}.tar.gz
Source0:	ansible-openstack-modules-%{githash}.tar.gz
BuildArch:      noarch

Requires:	ansible

%description
Unofficial Ansible modules for managing and deployment of OpenStack. Contains
all the necesary Neutron networking modules and also some Cinder, Glance,
Keystone and Nova modules missing in the official modules.


%prep
%setup -q -c


%build


%install
mkdir -p %{buildroot}%{_datadir}/ansible/ansible-openstack-modules
cp -a cinder* glance* keystone* neutron* nova* %{buildroot}%{_datadir}/ansible/ansible-openstack-modules/


%files
%doc LICENSE README.md
%{_datadir}/ansible/ansible-openstack-modules


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140912git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140911git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140910git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140909git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140908git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140907git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140906git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140905git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140904git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20140903git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Adam Samalik <asamalik@redhat.com> 0-20140902git79d751a
- new module: nova_flavor

* Thu Aug 28 2014 Adam Samalik <asamalik@redhat.com> 0-20140828git7611354
- packing with a license file

* Wed Aug 27 2014 Adam Samalik <asamalik@redhat.com> 0-20140827gitf543bea
- initial package
