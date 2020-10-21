%global debug_package %{nil}

Name:           bareftp
Version:        0.3.12
Release:        7%{?dist}
Summary:        File transfer client supporting the FTP, FTP over SSL/TLS (FTPS) and SSH


#  <spot> cassmodiah: okay, so the code from SharpSSH and JSch is BSD, the Banshee
#  bits are MIT, the Classpath bits are GPLv2+ with exceptions
#  <spot> cassmodiah: if you combine all of that with GPLv2 only code, you end up
#  with GPLv2 with exceptions
#  <spot> cassmodiah: feel free to put that in comments above the License tag to
#  explain it. :)

License:        GPLv2 with exceptions
URL:            http://www.bareftp.org/
Source0:        http://www.bareftp.org/release/%{name}-%{version}.tar.gz

BuildRequires:  gnome-sharp-devel
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  perl(XML::Parser)
BuildRequires:  gnome-desktop-sharp-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  gtk-sharp2-devel
BuildRequires:  mono-devel
BuildRequires:  gnome-keyring-sharp-devel
Buildrequires:  gcc

ExclusiveArch: %{mono_arches}


%description
bareFTP is a file transfer client supporting the FTP, FTP over SSL/TLS (FTPS)
and SSH File Transfer Protocol (SFTP). It is written in C#, targeting the Mono
framework and the GNOME desktop environment. bareFTP is free and open source
software released under the terms of the GPL license.

%prep
%setup -q

# Fixes for build with Mono 4
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
sed -i "s#mono/2.0#mono/4.5#g" configure

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


for file in $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
do
   desktop-file-validate $file
done

find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%find_lang %name

%files -f %{name}.lang
%doc AUTHORS COPYING CREDITS README
%dir %{_libdir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/bareftp*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.3.12-4
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.3.12-1
- 0.3.12

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-16
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-12
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.9-9
- Rebuild (mono4)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Dan Horák <dan[at]danny.cz> - 0.3.9-2
- updated supported arch list

* Sat Sep 24 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.3.9-1
- New release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.3.7-1
- new version 0.3.7

* Wed Oct 27 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.6-1
- New version 0.3.6
- Build against mono-2.8

* Mon Apr 19 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.3.2-1
- New Version 0.3.2

* Mon Jan 25 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.3.1-1
- New Version 0.3.1

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.2.3-4
- Exclude sparc64 no mono available

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.3-2
- fix buildrequires

* Sat Jun 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.3-1
- new version 0.2.3

* Sat May 30 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.2-3
- enable ppc64 build

* Sat Apr 11 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.2-2
- fix from rhbz #495001 Comment #1 From  Simon Wesp (cassmodiah@fedoraproject.org)
- include ExclusiveArch, disable creation of debuginfo package

* Wed Apr 08 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.2-1
- Initial RPM release
