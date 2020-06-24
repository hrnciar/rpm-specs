%global year  2013
%global month 03
%global day   01

Name:		julius-voxforge
Version:	%{year}.%{month}.%{day}
Release:	12%{?dist}
Summary:	VoxForge Acoustic Model files for Julius
License:	GPLv2+
URL:		http://www.voxforge.org/
Source0:	http://www.repository.voxforge1.org/downloads/Nightly_Builds/current/Julius-4.2-Quickstart-Linux_AcousticModel-%{year}-%{month}-%{day}.tgz
BuildArch:	noarch
Requires:	julius

%description
VoxForge was set up to collect transcribed speech for use with Free and
Open Source Speech Recognition Engines (on Linux, Windows and Mac).

%prep
%setup -q -c
sed -i 's/\r//' LICENSE

%build

%install
install -d %{buildroot}%{_datadir}/%{name}/acoustic
install -m644 acoustic_model_files/hmmdefs acoustic_model_files/macros acoustic_model_files/tiedlist %{buildroot}%{_datadir}/%{name}/acoustic

%files
%doc LICENSE README Sample.jconf
%{_datadir}/%{name}/acoustic

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2013.03.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.03.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.03.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.03.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Tom Callaway <spot@fedoraproject.org> - 2013.03.01-1
- update to 2013.03.01

* Sun Nov 11 2012 Huaren Zhong <huaren.zhong@gmail.com> - 2012.10.22
- Rebuild for Fedora
