Name:           xdffileio
Version:        0.3
Release:        12%{?dist}
Summary:        Unified interface to read/write EEG file format in realtime

License:        LGPLv3+
URL:            http://cnbi.epfl.ch/software/xdffileio.html
Source0:        https://github.com/nbourdau/xdffileio/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake autoconf
BuildRequires:  gnulib-devel

%description
xdffileio provides a unified interface to read/write EEG file format in
realtime. It has been designed to provide a consistent and common interface
to all supported file formats while minimizing the CPU cost on the main loop.
It thus performs all the expensive operation (scaling, data convertion and
file operation) in a separated thread.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
./autogen.sh

%configure \
%ifarch %{ix86}
        CFLAGS='%{optflags} -march=pentium4'
%endif

%make_build V=1

%install
%make_install

rm -f %{buildroot}%{_libdir}/lib%{name}.la
rm -vrf %{buildroot}%{_docdir}/%{name}

%check
make check V=1
rm -vrf doc/example/{.dirstamp,.deps,*.o}

%ldconfig_scriptlets

%files
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/example/
%{_includedir}/xdfio.h
%{_mandir}/man3/xdf_*.3*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar  5 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.3-3
- Build with $RPM_OPT_FLAGS on %%{ix86}

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3-1
- Initial package
