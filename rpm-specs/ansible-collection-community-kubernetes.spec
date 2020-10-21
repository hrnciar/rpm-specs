%global collection_namespace community
%global collection_name kubernetes

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Kubernetes Collection for Ansible

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/community.kubernetes/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible
BuildRequires:  python3-rpm-macros
Requires:       python%{python3_version}dist(openshift)

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n community.kubernetes-%{version}
rm -vr tests/integration molecule .github .yamllint codecov.yml setup.cfg
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md CHANGELOG.rst
%{ansible_collection_files}

%changelog
* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
