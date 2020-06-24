Name:           packETH
Version:        2.1
Release:        1%{?dist}
Summary:        A GUI packet generator tool

License:        GPLv2+
URL:            https://github.com/jemcek/packETH
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        packETH.desktop

BuildRequires:  gcc
BuildRequires:  autoconf automake
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel

%description
packETH is a Linux GUI tool that is able to send any packet or sequence of 
packets on the Ethernet. It uses the RAW socket option, so it doesn't care 
about ip, routing, etc. It is designed to have all the options available, 
with all the correct and incorrect values (incorrect means, that user can 
send wrong parameters like: incorrect checksum, wrong header length, etc.).

%prep
%autosetup

%build
# Build with new instructions from github
sed -i 's/^LIBS=/LIBS+=/' Makefile.am
sh autogen.sh
autoreconf -vfi
%configure
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
%make_install
# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/packeth

%changelog
* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Update to latest upstream release 2.1
- Update URLs
- Fix FTBFS (rhbz#1800185)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.0-1
- Update to 2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Nikolay Ulyanitsky <lystor AT gmail.com> - 1.7.2-1
- Update to 1.7.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Fri Oct 15 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.7-1
- Update to 1.7

* Sun Mar 07 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.6.5-3
- Fixed the license tag

* Fri Mar 05 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.6.5-2
- Fixed the Source URL

* Fri Mar 05 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.6.5-1
- Update to 1.6.5

* Fri Feb 19 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.6.4-0.2.dev
- Fix build error on F-13 with absent -lm in LIBS

* Sat Feb 13 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.6.4-0.1.dev
- Initial package build

