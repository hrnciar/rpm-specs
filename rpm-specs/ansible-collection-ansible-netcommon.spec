%global collection_namespace ansible
%global collection_name netcommon

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.1.2
Release:        1%{?dist}
Summary:        Ansible Network Collection for Common Code

# plugins/module_utils/compat/ipaddress.py: Python Software Foundation License version 2
# plugins/module_utils/network/common/config.py: BSD 2-clause "Simplified" License
# plugins/module_utils/network/common/netconf.py: BSD 2-clause "Simplified" License
# plugins/module_utils/network/common/network.py: BSD 2-clause "Simplified" License
# plugins/module_utils/network/common/parsing.py: BSD 2-clause "Simplified" License
# plugins/module_utils/network/common/utils.py: BSD 2-clause "Simplified" License
# plugins/module_utils/network/restconf/restconf.py: BSD 2-clause "Simplified" License
License:        GPLv3+ and BSD and Python
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.netcommon/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible >= 2.9.10
Requires:       ansible >= 2.9.10

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.netcommon-%{version}
sed -i -e '/version:/s/null/%{version}/' galaxy.yml
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -vr tests/integration bindep.txt .yamllint
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md
%{ansible_collection_files}

%changelog
* Sat Aug 08 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.2-1
- Initial package
