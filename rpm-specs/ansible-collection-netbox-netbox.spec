%global collection_namespace netbox
%global collection_name netbox

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Netbox modules for Ansible

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/netbox-community/ansible_modules/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible
BuildRequires:  python3-rpm-macros
Requires:       python%{python3_version}dist(pynetbox) >= 4.2.5

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible_modules-%{version}
sed -i -e '1{\@^#!.*@d}' plugins/modules/*.py
rm -vr tests/integration

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{ansible_collection_files}

%changelog
* Thu Jun 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun Apr 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Wed Mar 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Initial package
