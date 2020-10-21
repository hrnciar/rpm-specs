%global         snapshotdate 20140409
%global         commit d0971baf5d13e06aaa600581efe3adba6631e06a
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         checkout %{snapshotdate}git%{shortcommit}


Name:           check-create-certificate
Version:        0.5
Release:        19.%{checkout}%{?dist}
Summary:        A non-interactive script that creates an SSL certificate if it does not exist
License:        GPLv2
Url:            https://github.com/jdsn/check-create-certificate
Source:         https://github.com/jdsn/check-create-certificate/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:         perl-generators
Requires:       openssl-perl
BuildArch:      noarch

%description
A script that checks for the existence of an SSL certificate
or creates a new self signed one. It runs non-interactively and
uses either predefined values or automatically guesses the best values.


%prep
%setup -qn %{name}-%{commit}

%build

%install
install -Dpm 755 script/%{name} %{buildroot}%{_sbindir}/%{name}

%files
%{_sbindir}/%{name}
%doc COPYING

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.5-10.20140409gitd0971ba
- Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8.20140409gitd0971ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-7.20140409gitd0971ba
- corrected commit name in %%setup section
- removed checkout instructions

* Fri Apr 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-6.20140409gitd0971ba
- corrected snapshotdate
- corrected source url
- corrected git command
- droped %%install command for doc file in %%install section
- correted spelling in %%description

* Thu Apr 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-5.20140409gitd0971ba
- droped coreutils, perl BuildRequires
- replaced openssl by openssl-perl BuildRequires
- added -p option to preserver the timestamp in install section
- changed doc macro in files section 
- used git commit for package version

* Wed Apr 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-4
- removed attr in file section

* Wed Apr 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-3
- checked out new sources 
- removed fsf-fix patch
- changed to new Url address

* Wed Apr 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.5-2
- Added fsf-fix patch that fixes rpmlint error
- specfile cleanup

