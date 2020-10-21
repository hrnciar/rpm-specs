Name:           python-beniget
Version:        0.3.0
Release:        1%{?dist}
Summary:        Extract semantic information about static Python code
License:        BSD
URL:            https://github.com/serge-sans-paille/beniget/
Source0:        %{url}/archive/%{version}/beniget-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
A static analyzer for Python2 and Python3 code.Beniget provides a static over-
approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each definition.}
%description %_description


%package -n     python3-beniget
Summary:        %{summary}

%description -n python3-beniget %_description


%prep
%autosetup -n beniget-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files beniget


%check
%tox


%files -n python3-beniget -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Mon Sep 14 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-1
- Update to 0.3.0
- Fixes rhbz#1878161

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- Initial package
