%global	module	kyotocabinet

Name:		python-%{module}
Version:	1.22
Release:	3%{?dist}
# https://fallabs.com/kyotocabinet/pythondoc/kyotocabinet-module.html
License:	GPLv3
Summary:	Kyoto Cabinet Python bindings
URL:		https://fallabs.com/kyotocabinet/
Source0:	https://fallabs.com/kyotocabinet/pythonpkg/%{module}-python-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	python3-setuptools
# python3-devel
BuildRequires:	pkgconfig(python3)
# zlib-devel
BuildRequires:	pkgconfig(zlib)
# kyotocabinet-devel
BuildRequires:	pkgconfig(kyotocabinet)

%description
Kyoto Cabinet is a library of routines for managing a key-value database.

%package -n	python3-%{module}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
Kyoto Cabinet is a library of routines for managing a key-value database.

%prep
%autosetup -n %{module}-python-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc README doc/ example/
%{python3_sitearch}/Kyoto_Cabinet-1.5-py*.egg-info
%{python3_sitearch}/kyotocabinet*.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 TI_Eugene <ti.eugene@gmail.com> - 1.22-2
- Spec fixes

* Mon Jun 08 2020 TI_Eugene <ti.eugene@gmail.com> - 1.22-1
- Initial build
