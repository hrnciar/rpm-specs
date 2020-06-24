Name:           libserialport
Version:        0.1.1
Release:        8%{?dist}
Summary:        Library for accessing serial ports
License:        LGPLv3+
URL:            http://sigrok.org/wiki/%{name}
Source0:        http://sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc

Provides: bundled(jquery) = 1.7.1

%description
libserialport is a minimal library written in C that is intended to take care
of the OS-specific details when writing software that uses serial ports.

By writing your serial code to use libserialport, you enable it to work
transparently on any platform supported by the library.

The operations that are supported are:

- Port enumeration (obtaining a list of serial ports on the system).
- Opening and closing ports.
- Setting port parameters (baud rate, parity, etc).
- Reading, writing and flushing data.
- Obtaining error information.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.


%prep
%setup -q

%build
%configure --disable-static
V=1 make %{?_smp_mflags}

# This builds documentation for the -doc package
make %{?_smp_mflags} doc


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING README
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc doxy/html-api/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 mrnuke <mr.nuke.me@gmail.com> - 0.1.1-0
- Update to libserialport 0.1.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 25 2014 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-1
- Updated sources to official libserialport release
- Added "Provides" for bundled jquery

* Wed Mar 12 2014 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-0.3.20140110git3ceb8ae
- Remove empty doc macro from devel subpackage
- Make doc subpackage dependent on main package
- Document archive generation process and regenerate source archive
- Use _smp_mflags macro when building doc to silence fedora-review

* Sat Mar 08 2014 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-0.2.20140110git3ceb8ae
- Add doxygen-generated documentation in doc subpackage
- Use explicit soversion in files section
- Update sources to lastest git snapshot (3ceb8ae)

* Fri Nov 22 2013 Dan Horák <dan[at]danny.cz> - 0.1.0-0.1.20131122git
- initial Fedora version
