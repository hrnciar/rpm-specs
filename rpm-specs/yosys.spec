#%%global commit0 8a4c6e6563eea979dc96cada14abb08d63a8e3d1
#%%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})

#%%global snapdate 20190826

%global __python %{__python3}

Name:           yosys
Version:        0.9
Release:        4%{?dist}
#Release:        1.1.%%{snapdate}git%%{shortcommit0}%%{?dist}
Summary:        Yosys Open SYnthesis Suite, including Verilog synthesizer
License:        ISC and MIT
URL:            http://www.clifford.at/yosys/

Source0:        https://github.com/YosysHQ/%{name}/archive/%{name}-%{version}.tar.gz
#Source0:        https://github.com/YosysHQ/%%{name}/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
Source1:        https://github.com/mdaines/viz.js/releases/download/0.0.3/viz.js

# man pages written for Debian:
Source2:        http://http.debian.net/debian/pool/main/y/yosys/yosys_0.9-1.debian.tar.xz
# requested that upstream include those man pages:
#   https://github.com/YosysHQ/yosys/issues/278

# Fedora-specific patch:
# Change the substitution done when making yosys-config so that it outputs
# CXXFLAGS with -I/usr/include/yosys
Patch1:         yosys-cfginc.patch

# Fedora-specific patch:
# When invoking yosys-config for examples in "make manual", need to use
# relative path for includes, as they're not installed in build host
# filesystem.
Patch2:         yosys-mancfginc.patch

BuildRequires:  gcc-c++
BuildRequires:  bison flex readline-devel pkgconfig
BuildRequires:  tcl-devel libffi-devel
BuildRequires:  abc >= 1.01-9
BuildRequires:  iverilog
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  txt2man

# required for documentation:
BuildRequires:  graphviz
BuildRequires:  texlive-beamer
BuildRequires:  texlive-collection-bibtexextra
BuildRequires:  texlive-collection-fontsextra
BuildRequires:  texlive-collection-latexextra
BuildRequires:  texlive-collection-publishers
BuildRequires:  texlive-collection-science

Requires:       %{name}-share = %{version}-%{release}
Requires:       graphviz python-xdot
Requires:       abc >= 1.01-9


%description
Yosys is a framework for Verilog RTL synthesis. It currently has
extensive Verilog-2005 support and provides a basic set of synthesis
algorithms for various application domains.


%package doc
Summary:        Documentation for Yosys synthesizer

%description doc
Documentation for Yosys synthesizer.


%package share
Summary:        Architecture-independent Yosys files
BuildArch:      noarch

%description share
Architecture-independent Yosys files.


%package devel
Summary:        Development files to build Yosys synthesizer plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tcl-devel

%description devel
Development files to build Yosys synthesizer plugins.


%prep
%setup -q -n %{name}-%{name}-%{version}
#%%setup -q -n %%{name}-%%{commit0}

%patch1 -p1 -b .cfginc
%patch2 -p1 -b .mancfginc

# Ensure that Makefile doesn't wget viz.js
cp %{SOURCE1} .

# Get man pages from Debian
%setup -q -T -D -a 2 -n %{name}-%{name}-%{version}
#%%setup -q -T -D -a 2 -n %%{name}-%%{commit0}

# In all Python shebang lines, remove use of /usr/bin/env,
# without changing timestamps
for f in `find . -name \*.py`
do
    sed 's|/usr/bin/env python3|/usr/bin/python3|' $f >$f.new
    touch -r $f $f.new
    mv $f.new $f
done

make config-gcc

# Change manual source files to use libertine font rather than non-free
# luximono
for f in `find manual -name \*.tex -exec grep -l {luximono} {} \;`
do
    sed -i 's|{luximono}|{libertine}|' $f
done


%build
%set_build_flags
make %{?_smp_mflags} PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc PRETTY=0 all manual

%global man_date "`stat -c %y debian/man/yosys-smtbmc.txt | awk '{ print $1 }'`"
txt2man -d %{man_date} -t YOSYS-SMTBMC debian/man/yosys-smtbmc.txt >yosys-smtbmc.1


%install
%make_install PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc STRIP=/bin/true

# move include files to includedir
install -d -m0755 %{buildroot}%{_includedir}
mv %{buildroot}%{_datarootdir}/%{name}/include %{buildroot}%{_includedir}/%{name}

# install man mages
install -d -m0755 %{buildroot}%{_mandir}/man1
install -m 0644 yosys-smtbmc.1 debian/yosys{,-config,-filterlib}.1 %{buildroot}%{_mandir}/man1

# install documentation
install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 manual/*.pdf %{buildroot}%{_docdir}/%{name}

%check
make test ABCEXTERNAL=%{_bindir}/abc SEED=314159265359


%files
# license texts requested upstream:
#   https://github.com/YosysHQ/yosys/issues/263
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-filterlib
%{_bindir}/%{name}-smtbmc
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-filterlib.1*
%{_mandir}/man1/%{name}-smtbmc.1*

%files share
%{_datarootdir}/%{name}

%files doc
%{_docdir}/%{name}

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_mandir}/man1/%{name}-config.1*


%changelog
* Thu Apr 23 2020 Dan Horák <dan[at]danny.cz> - 0.9-4
- updated Requires for yosys-devel

* Sun Apr 19 2020 Marcus A. Romer <aimylios@gmx.de> - 0.9-3
- Update man pages from Debian
- Add license text

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9-1
- Update to latest release
- Spec file cleanup

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8-4
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Jon Burgess <jburgess777@gmail.com> - 0.8-2
- Add buildreq for g++

* Sat Oct 27 2018 Jon Burgess <jburgess777@gmail.com> - 0.8-1
- Updated to latest upstream release
- Make sure package built with Fedora compile flags
- Fix assert while running tests
- Fixes FTBFS #1606769

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.7-9
- rebuilt due new iverilog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7-3
- Rebuild for readline 7.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7-2
- Rebuild for Python 3.6

* Sat Nov 26 2016 Eric Smith <brouhaha@fedoraproject.org> 0.7-1
- Updated to latest upstream release.
- Additional changes per package review.

* Fri Nov 04 2016 Eric Smith <brouhaha@fedoraproject.org> 0.6.0-2.20160923git8f5bf6d
- Updated per Randy Barlow's package review comments of 2016-10-20.

* Sat Sep 24 2016 Eric Smith <brouhaha@fedoraproject.org> 0.6.0-1.20160923git8f5bf6d
- Initial version (#1375765).
