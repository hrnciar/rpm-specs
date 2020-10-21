# Review: https://bugzilla.redhat.com/show_bug.cgi?id=445140

%global	use_release	1
%global	use_gitbare 	0

%if 0%{?use_gitbare} < 1
# force
%global	use_release 	1
%endif

%if 0%{?use_gitbare}
%global	gittardate		20190301
%global	gittartime		2144
%global	gitbaredate	20190224
%global	git_rev		db6017ff991f298b7a362ce5acbdd4d84cf40b18
%global	git_short		%(echo %{git_rev} | cut -c-8)
%global	git_version	D%{gitbaredate}git%{git_short}
%endif

%global	mainrel		2

%if 0%{?use_release} >= 1
%global         fedorarel   %{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif
%if 0%{?use_gitbare} >= 1
%global         fedorarel   %{mainrel}.%{git_version}
%endif

Name:           lxtask
Version:        0.1.9
Release:        %{fedorarel}%{?dist}.2
Summary:        Lightweight and desktop independent task manager

License:        GPLv2+
URL:            http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
# https://sourceforge.net/p/lxde/patches/535/
Patch0:			https://sourceforge.net/p/lxde/patches/535/attachment/lxtask-fix-no-common.patch

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  pkgconfig(gtk+-2.0) > 2.6
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
%if 0%{?use_gitbare}
BuildRequires:  automake
BuildRequires:  libtool
%endif


%description
LXTask is a lightweight task manager derived from xfce4 task manager with all
xfce4 dependencies removed, some bugs fixed, and some improvement of UI. 
Although being part of LXDE, the Lightweight X11 Desktop Environment, it's 
totally desktop independent and only requires pure gtk+.


%prep
%if 0%{?use_release}
%setup -q %{?git_version:-n %{name}-%{version}-%{?git_version}}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{version}-fedora %{git_rev}
cp -a [A-Z]* ..
%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-owner@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

%patch0 -p1
git commit -m "Apply upstream tracker proposal patch" -a

%build
%if 0%{?use_gitbare}
cd %{name}
bash autogen.sh
%endif

%configure
make %{?_smp_mflags}


%install
%if 0%{?use_gitbare}
cd %{name}
%endif

make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install \
    %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
    %endif
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/lxtask.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.9-2
- Apply upstream track proposal patch for gcc10 -fno-common

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.9-1
- 0.1.9 formal release

* Fri Mar  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-10.D20190224gitdb6017ff
- Update to the latest git

* Mon Feb 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-9
- Upstream patch for correcting "free memory" usage display

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-5
- Make renice process work (SF#889)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.8-1
- 0.1.8

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.7-1
- 0.1.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.6-1
- 0.1.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-6
- Fix desktop vendor conditionals

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.4-5
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-2
- Support full cmdline (LXDE #3469683)
- Close dialog with Escape button or CTRL+W (LXDE #3490254)
- Don't resize columns automatically
- Fix integer overflow
- Update translations from Pootle

* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4
- Fix crash (#732182)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.3-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 15 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Tue Apr 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Jul 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Mon Feb 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-2
- Fix categories in desktop file

* Sun May 04 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial Fedora RPM
