Name:           mpdas
Version:        0.4.4
Release:        9%{?dist}
Summary:        An MPD audioscrobbling client

License:        BSD
URL:            http://50hz.ws/%{name}/
Source0:        http://50hz.ws/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libcurl-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  gcc-c++
Provides:       bundled(md5-deutsch)

%description
mpdas is a MPD AudioScrobbler client supporting the 2.0 protocol
specs. It is written in C++ and uses libmpd to retrieve the song
data from MPD and libcurl to post it to Last.fm


%prep
%setup -q

%build
export CONFIG="%{_sysconfdir}" PREFIX="%{buildroot}%{_prefix}" MANPREFIX="%{buildroot}%{_mandir}" CXXFLAGS+="$RPM_OPT_FLAGS"
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_mandir}/man1/ %{buildroot}%{_sysconfdir} %{buildroot}%{_bindir}

# Manually install them
install -m 0755 mpdas %{buildroot}%{_bindir}/mpdas
rm mpdas -f
install -m 0644 mpdas.1 %{buildroot}%{_mandir}/man1/mpdas.1

%files
%doc README mpdasrc.example
%license LICENSE
%{_mandir}/man1/mpdas.1*
%{_bindir}/mpdas

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.4-3
- Add gcc-c++ to BRs
- Use buildroot instead of RPM_BUILD_ROOT

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.4-1
- Update to latest upstream release

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 0.4.2-5
- Rebuilt for new libmpdclient

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-1
- Update to latest upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for c++ ABI breakage

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-3
- spec bump for gcc 4.7 rebuild

* Thu Apr 14 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-2
- Changed make flags

* Mon Mar 14 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org>-  0.3.0-2
- Added virtual requires for md5-deutshc

* Sat Feb 26 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-2
- add a patch to fix a minor glitch in the man page

* Sat Feb 26 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-1
- Initial rpm build
