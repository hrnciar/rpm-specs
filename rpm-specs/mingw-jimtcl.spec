%?mingw_package_header

%global name1 jimtcl
Name:           mingw-%{name1}
Version:        0.79
Release:        2%{?dist}
Summary:        MinGW small embeddable Tcl interpreter

License:        BSD
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name1}/archive/%{version}/%{name1}-%{version}.tar.gz
# install documentation into /usr/share/doc/mingw{32,64}-jimtcl instead of
# /usr/{i686,x86_64}-w64-mingw32/sys-root/mingw/lib/mingw{32,64}-jimtcl
# patch from the native jimtcl package
Patch0:         jimtcl-fix_doc_paths.patch
# install libjim.dll into bindir (instead of libdir), and install the implib
# libjim.dll.a into libdir, to comply with mingw packaging guidelines
Patch1:         jimtcl-implib.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  asciidoc
BuildRequires:  gcc

%description
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw32-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw32-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw64-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw64-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%{?mingw_debug_package}

%prep
%setup -q -n %{name1}-%{version}
%patch0 -p0 -b .doc
%patch1 -p0 -b .implib

%build
%mingw_configure --full --shared --disable-option-checking

%mingw_make %{?_smp_mflags}


%install
install -d %{buildroot}/%{mingw32_datadir}/doc/%{name1}
install -d %{buildroot}/%{mingw64_datadir}/doc/%{name1}
%mingw_make install DESTDIR=%{buildroot} INSTALL_PROGRAM="cp -p" INSTALL_DATA="cp -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}/%{mingw32_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw64_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw32_datadir}/%{mingw32_prefix}/docs
rm -rf %{buildroot}/%{mingw64_datadir}/%{mingw64_prefix}/docs
rm -rf %{buildroot}/%{mingw32_libdir}/jim/tcltest.tcl
rm -rf %{buildroot}/%{mingw64_libdir}/jim/tcltest.tcl
install -d %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{mingw32_bindir}/build-jim-ext
rm -f %{buildroot}/%{mingw64_bindir}/build-jim-ext

%files -n mingw32-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw32_bindir}/jimsh.exe
%{mingw32_bindir}/libjim.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libjim.dll.a
%{mingw32_libdir}/pkgconfig/jimtcl.pc

%files -n mingw64-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw64_bindir}/jimsh.exe
%{mingw64_bindir}/libjim.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libjim.dll.a
%{mingw64_libdir}/pkgconfig/jimtcl.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.79-1
- update

* Wed May 01 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.78-1
- update

* Fri Mar 23 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.77-1
- update

* Tue Feb 14 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.76-2
- remove BuildRoot and clean sections

* Fri Feb 03 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.76-1
- Initial Specfile
