# Review: https://bugzilla.redhat.com/show_bug.cgi?id=448236

Name:           xfbib
Version:        0.1.0
Release:        13%{?dist}
Summary:        Lightweight BibTeX editor for the Xfce desktop environment
Summary(de):    Schlanker BibTeX Editor für die Xfce Desktop-Umgebung

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://git.xfce.org/apps/xfbib/snapshot/%{name}-%{version}.tar.bz2

BuildRequires:  gtk2-devel >= 2.10
BuildRequires:  libxfce4ui-devel >= 4.4.0
BuildRequires:  libxfce4util-devel >= 4.4.0
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
# Need these until there's a real release
BuildRequires:  xfce4-dev-tools libtool

%description
Xfbib is a lightweight BibTeX editor developed for the Xfce desktop 
environment. The intention of Xfbib is to provide an easy and efficient way 
of editing BibTeX files. 

%description -l de
Xfbib ist ein schlanker BibTex Editor, der für die Xfce Desktop-Umgebung 
entwickelt wird. Das Ziel von Xfbib ist es, einen einfachen und effizienten 
Weg zum Bearbeiteiten von BibTeX Dateien zur Verfügung zu stellen.


%prep
%setup -q

%build
xdt-autogen
%configure --disable-static
make %{?_smp_mflags} install='INSTALL -p'


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
%find_lang %{name}

desktop-file-install \
    %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
    %else
    --vendor="" \
    %endif
    --add-category X-Xfce \
    --remove-category Application \
    --remove-key Encoding \
    --remove-key GenericName \
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/xfbib

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 0.1.0-1
- Update to 0.1.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.2-10
- Make desktop vendor conditional
- Add aarch64 support (#926768)
- Spec file clean-up
- Update scriptlets

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.0.2-9
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.0.2-7
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.2-5
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 24 2008 Christoph Wickert <fedora christoph-wickert de> - 0.0.2-1
- Initial Fedora package
