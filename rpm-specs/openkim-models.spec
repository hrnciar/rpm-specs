Name:           openkim-models
Version:        2019.07.25
%global         uversion %(v=%{version}; echo ${v//./-})
Release:        4%{?dist}
Summary:        Open Knowledgebase of Interatomic Models
License:        CDDL-1.0 and ASL 2.0 and MPLv2.0 and GPLv3 and LGPLv3
Url:            https://openkim.org
Source0:        https://s3.openkim.org/archives/collection/%{name}-%{uversion}.txz
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  cmake3 >= 3.4
BuildRequires:  kim-api-devel >= 2.1.0
BuildRequires:  vim

%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the models from openkim.org.

%prep
%setup -q -n %{name}-%{uversion}

%build
%{cmake3} -DCMAKE_SKIP_RPATH=ON ..
%cmake_build

%install
%cmake_install
# Each model-driver and model is licensed separately.
# About 2/3 are CDDL-1.0, 1/4 public domain, and 1/12 GPL/LGPL
for i in $(find *model* -name "LICENSE*"); do echo ${i%/*}:; head -n 2 $i; echo;  done > LICENSE.models

%files
%license LICENSE LICENSE.models
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/portable-models/
%{_libdir}/kim-api/simulator-models/

%changelog
* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 2019.07.25-4
- Fix out-of-source build on F33 (bug#1865159)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.25-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Ryan S. Elliott <relliott@umn.edu> - 2019.07.25-1
- Version bump to 2019.07.25

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.03.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.03.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Christoph Junghans <junghans@votca.org> - 2019.03.31-2
- Comments from review (bug #1703235)

* Wed Apr 24 2019 Christoph Junghans <junghans@votca.org> - 2019.03.31-1
- initial commit
