# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442269

%global git_snapshot 0

%if 0%{?git_snapshot}
%global git_rev f0945814186b2903c9899e8d91e640e3341fd2b9
%global git_date 20100903
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

# Source0 was generated as follows: 
# git clone git://lxde.git.sourceforge.net/gitroot/lxde/%{name}
# cd %{name}
# git archive --format=tar --prefix=%{name}/ %{git_short} | bzip2 > %{name}-%{?git_version}.tar.bz2
 
Name:           lxappearance
Version:        0.6.3
Release:        11%{?git_version:.%{?git_version}}%{?dist}
Summary:        Feature-rich GTK+ theme switcher for LXDE

License:        GPLv2+
URL:            http://lxde.org/
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxappearance
%if 0%{?git_snapshot}
Source0:        %{name}-%{?git_version}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
# https://sourceforge.net/p/lxde/bugs/866/
Patch0:		https://sourceforge.net/p/lxde/bugs/_discuss/thread/ecb5ef0c/9b37/attachment/lxappearance-0.6.3-icon-theme-init.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0) > 2.6
BuildRequires:	  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
Requires:       lxsession >= 0.4.0

%description
LXAppearance is a new GTK+ theme switcher developed for LXDE, the Lightweight 
X11 Desktop Environment. It is able to change GTK+ themes, icon themes, and 
fonts used by applications. All changes done by the users can be seen 
immediately in the preview area. After clicking the "Apply" button, the 
settings will be written to gtkrc, and all running programs will be asked to 
reload their themes.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing plug-ins 
for LXAppearance.


%prep
%setup -q %{?git_version:-n %{name}}
%patch0 -p1 -b .init


%build
%{?git_version:sh autogen.sh}
%configure \
	--enable-dbus \
	--disable-silent-rules \
	%{nil}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install \
    %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
    %endif
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-3
- Fix non-initialized variable usage detected by clang
  (sourceforge bug 866)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-1
- 0.6.3

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.2-1
- 0.6.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1-1
- 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-5
- Fix desktop vendor conditionals
- Make build verbose

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.5.2-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (#827780)

* Sun Mar 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 (includes manpage again)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.0-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Sep 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.20100903gitf0945814
- Update to GIT preview of 0.5.0

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Add patch to fix DSO linking (#564754)

* Thu Jan 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Dec 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Nov 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Workaround for infinite loop that causes FTBFS (#538963)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Apr 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2-1
- Update to 0.2
- Remove install-patch, applied upstream

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial Fedora RPM
