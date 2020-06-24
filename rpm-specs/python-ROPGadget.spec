%global srcname ROPGadget

Name:           python-%{srcname}
Version:        6.3
Release:        3%{?dist}
Summary:        A tool to find ROP gadgets in program files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/R/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/LICENSE_BSD.txt
Source2:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/README.md

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist capstone}

%description
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       %{py3_dist capstone}

%description -n python3-%{srcname}
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%prep
%autosetup -n %{srcname}-%{version}
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%build
%py3_build

%install
%py3_install
for lib in $(find %{buildroot}%{python3_sitelib}/ropgadget/ -name "*.py"); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%files -n python3-%{srcname}
%doc LICENSE_BSD.txt README.md
%{python3_sitelib}/ropgadget
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{_bindir}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.3-3
- Rebuilt for Python 3.9

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 6.3-2
- Commit copy of README.md and LICENSE_BSD.txt

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 6.3-1
- New upstream version
- Reflect change to license

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 W. Michael Petullo <mike@flyn.org> - 5.8-1
- New upstream version

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4-6
- Subpackage python2-ROPGadget has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 5.4-1
- Initial package
