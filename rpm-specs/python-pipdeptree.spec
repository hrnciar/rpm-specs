%global srcname pipdeptree

%global _description\
pipdeptree is a command line utility for displaying the installed python\
packages in form of a dependency tree. It works for packages installed\
globally on a machine as well as in a virtualenv.

Name:           python-%{srcname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Command line utility to show dependency tree of packages

License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
Source0:        https://github.com/naiquevin/pipdeptree/archive/%{version}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} graphviz

%prep
%autosetup -n %{srcname}-%{version}

# Remove pinned versions from tox.ini
# Upstream already did the same in master branch
# https://github.com/naiquevin/pipdeptree/commit/bcc7f4308a3371d62eca28eff680b48ab7b112ff#diff-b91f3d5bd63fcd17221b267e851608e8
sed -i "s/\(.*\)==.*/\1/" tox.ini

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.rst
%{_bindir}/pipdeptree

%changelog
* Tue Sep 08 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1846897)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.2-1
- Fix Bug #1697089 - Bump version to 0.13.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.1-2
- Bump version to 0.13.1 and ignore tests

* Sat Jun 30 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.12.1-1
- Initial package.
