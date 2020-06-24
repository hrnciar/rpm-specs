Name:			liblinear
Version:		1.94
Release:		24%{?dist}
Summary:		Library for Large Linear Classification
%{?el5:Group:		System Environment/Libraries}

License:		BSD
URL:			http://www.csie.ntu.edu.tw/~cjlin/%{name}
Source0:		%{url}/%{name}-%{version}.tar.gz
Source1:		%{url}/index.html
Source2:		%{url}/FAQ.html
Source3:		%{url}/exp.html
Source4:		http://www.csie.ntu.edu.tw/~cjlin/papers/%{name}.pdf

# simple fixes, not needed by upstream
Patch0:			liblinear-adapt_makefile.patch
Patch1:			liblinear-fix_compiler_warnings.patch

%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:  gcc-c++
BuildRequires:		blas-devel


%description
%{name} is an open source library for large-scale linear classification.
It supports logistic regression and linear support vector machines.  It
provides easy-to-use command-line tools and library calls for users and
developers.  Comprehensive documents are available for both beginners
and advanced users.

Experiments demonstrate that %{name} is very efficient on large sparse
data sets.  %{name} is the winner of ICML 2008 large-scale learning
challenge (linear SVM track).  It is also used for winning KDD Cup 2010.

%ldconfig_scriptlets

%files
%doc COPYRIGHT
%{_libdir}/%{name}.so.*


%package cli
Summary:		CLI-tools for %{name}
%{?el5:Group:		Applications/Engineering}

Requires:		%{name}%{?_isa}		== %{version}-%{release}

%description cli
This package contains cli-tools for use with %{name}.

For further information read "3.1 Practical Usage" from the pdf included
in the %{name}-doc package.

%files cli
%doc heart_scale
%{_bindir}/*


%package devel
Summary:		Development files for %{name}
%{?el5:Group:		Development/Libraries}

Requires:		%{name}%{?_isa}		== %{version}-%{release}
%{?el5:Requires:	%{_bindir}/pkg-config}

%{?el5:Provides:	pkgconfig(%{name})	== %{version}}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%package doc
Summary:		Documentation files for %{name}
%{?el5:Group:		Documentation}

%{!?el5:BuildArch:	noarch}

%description doc
The %{name}-doc package contains some brief documentation for developing
applications that use %{name}.

%files doc
%doc COPYRIGHT README* {predict,train}.c *.html *.pdf

%if 0%{?fedora} || 0%{?rhel} >= 8
%package -n python3-%{name}
Summary:		Python3 bindings for %{name}

BuildRequires:		python3-devel
Requires:		%{name}%{?_isa}		== %{version}-%{release}

%description  -n python3-%{name}
This package contains bindings for developing Python3 applications that
use %{name}.

For further information read "README.python" included in the
%{name}-doc package.

%files -n python3-%{name}
%{python3_sitearch}/*
%endif #0%{?fedora} || 0%{?rhel} >= 8


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# pull in other sources
install -pm 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

# remove bundled stuff
rm -rf blas/ matlab/ windows/ Makefile.*

# add pkg-config file
cat << EOF >> %{name}.pc
#################################
# Pkg-Config file for %{name} #
#################################

Name: %{name}
Description: Library for Large Linear Classification
URL: %{url}
Version: %{version}

prefix=%{_prefix}
includedir=%{_includedir}

Cflags: -I\$\{includedir\}/liblinear
Libs: -llinear
EOF

# rename python/README for inclusion in doc
mv python/README README.python

# remove hashbang from lib's files
for _file in python/*.py
do
  sed '1{\@^#!/usr/bin/env python@d}' ${_file} > ${_file}.new &&
  touch -r ${_file} ${_file}.new &&
  mv -f ${_file}.new ${_file}
done


%build
# Fortran doesn't like as-needed
%undefine _ld_as_needed

%configure ||:
make %{?_smp_mflags}


%install
%{?el5:rm -rf %{buildroot}}

# no install-target in Makefile
mkdir -p %{buildroot}%{_bindir}			\
	%{buildroot}%{_libdir}/pkgconfig	\
	%{buildroot}%{_includedir}/%{name}

install -pm 0755 predict %{buildroot}%{_bindir}/%{name}-predict
install -pm 0755 train %{buildroot}%{_bindir}/%{name}-train
install -pm 0755 %{name}.so.1 %{buildroot}%{_libdir}
ln -s %{name}.so.1 %{buildroot}%{_libdir}/%{name}.so
install -pm 0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig
install -pm 0644 {linear,tron}.h %{buildroot}%{_includedir}/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 8
mkdir -p %{buildroot}%{python3_sitearch}
install -pm 0644 python/*.py %{buildroot}%{python3_sitearch}
%endif #0%{?fedora} || 0%{?rhel} >= 8



%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.94-24
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.94-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.94-21
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 1.94-18
- Remove Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.94-16
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.94-14
- Python 2 binary package renamed to python2-liblinear
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.94-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.94-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun May 04 2014 Björn Esser <bjoern.esser@gmail.com> - 1.94-1
- new upstream release (#1051090)
- failsafe backport of Python2-macros for RHEL <= 6
- Python3 is not available on RHEL7, yet
- preserve timestamps of modified files
- minor improvements

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 1.93-3
- adaptions for new Python-guidelines
- generate .pc-file on-the-fly
- minor cleanup

* Mon Aug 12 2013 Björn Esser <bjoern.esser@gmail.com> - 1.93-2
- build arched python-plugins
- nuke hashbang from python-plugins

* Sun Aug 11 2013 Björn Esser <bjoern.esser@gmail.com> - 1.93-1
- Initial rpm release (#995864)
