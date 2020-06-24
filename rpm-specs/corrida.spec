%define version_major 0.96
%define version_minor 11

Name:           corrida
Version:        %{version_major}.%{version_minor}
Release:        26%{?dist}
Summary:        Application for archivation of meteor observations

License:        GPLv2
URL:            http://corrida.pkim.org/
Source0:        http://corrida.pkim.org/releases/corrida-%{version_major}-%{version_minor}.tar.gz
Source1:        corrida.desktop
Patch0:         corrida-0.96-11-count.patch
# Sent by e-mail to jurmcc@gmail.com
Patch1:         corrida-0.96-11-formatsec.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils

%description
Application was designed by Polish Fireball Center cooperators to ease
archivation of meteor observations.


%prep
%setup -q -n corrida-%{version_major}-%{version_minor}
%patch0 -p1 -b .count
%patch1 -p1 -b .formatsec


%build
find . -type f |xargs chmod 0644
make %{?_smp_mflags} PREFIX=%{_prefix}/ CFLAGS="%{optflags}"
convert common/corrida.ico corrida.png


%install
make install PREFIX=%{buildroot}%{_prefix}/

# Directory structure
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications

# Icon
install -pm 0644 corrida.png %{buildroot}%{_datadir}/pixmaps

# Menu entry
desktop-file-install %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications

%files
%{_bindir}/corrida
%{_bindir}/torero
%{_datadir}/corrida
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%doc copying


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.96.11-14
- Fix build with -Werror=format-security

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.96.11-13
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.96.11-11
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.96.11-7
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.96.11-4
- Automatically increment the meteor number (#494526)

* Tue Mar 24 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.96.11-3
- Fix the menu categories

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.96.11-1
- Initial packaging attempt
