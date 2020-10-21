# Force out of source build
%undefine __cmake_in_source_build

Name:           partio
Version:        1.13.0
Release:        1%{?dist}
Summary:        Library for reading/writing/manipulating common animation particle

License:        BSD
URL:            https://www.partio.us
Source:         https://github.com/wdas/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Versioning libraries
# https://github.com/wdas/partio/issues/82
Patch:          %{name}-version-libraries.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gl)
%if 0%{?fedora} < 32
BuildRequires:  freeglut-devel
%else
BuildRequires:  pkgconfig(glut)
%endif
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  swig

%description
C++ (with python bindings) library for easily reading/writing/manipulating 
common animation particle formats such as PDB, BGEO, PTC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
%{summary}

%package        libs
Summary:        Core %{name} libraries

%description    libs
%{description}

%package -n python3-%{name}
Summary:        %{summary}
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name} 
The python3-%{name} contains Python 3 binning for the library.

#%%package test
#Summary: Run-time component of %%{name} test library
#%%description test
#Run-time support for simple program testing, full unit testing, and for
#program execution monitoring.

%prep
%autosetup -p1

# Fix all Python shebangs recursively in .
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%cmake \
 -DCMAKE_PREFIX_PATH=%{_prefix} \
.
%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#Remove files from unversioned python directory
rm -f %{buildroot}%{_libdir}/python/site-packages/*.py

#Remove all tests containing arch-depedents binaries
rm -rf %{buildroot}%{_datadir}/%{name}/test

%files
%license LICENSE
%doc README.md
%{_bindir}/part*
%{_datadir}/swig/%{name}.i
%dir %{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_defaultdocdir}/%{name}/html

%files libs
%license LICENSE
%{_libdir}/*.so.{1,%{version}}

%files -n python3-%{name}
%{python3_sitearch}/_%{name}.so
%pycached %{python3_sitearch}/*.py

#%%files test
#%%dir %%{_datadir}/%%{name}/test
#%%{_datadir}/%%{name}/test/*

%changelog
* Sat Sep 12 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.13.0-1
- Update to 1.10.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.10.1-3
- Set conditional buildrequire of glut for Fedora 31 and less
- Set versioning libraries

* Sat Jul 18 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.10.1-2
- Fix spec according to the review (#1858531)
- Remove arch-dependeants libraries from /usr/share

* Sat May 30 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.10.1-1
- Initial build
