%define		mainver		0.7.1
%define		vendorrel	8
%define		repoid		18105



Name:		kreetingkard
Version:	%{mainver}
Release:	%{vendorrel}%{?dist}.3
Summary:	Japanese greeting card writing software for KDE

License:	GPLv2+
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:	http://downloads.sourceforge.jp/%{name}/%{repoid}/%{name}-%{mainver}.tar.gz
# From Mandriva
Patch0:		kreetingkard-0.7.1-fix-build-gcc411.patch

BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
%if 0%{fedora} >= 8
BuildRequires:	kdelibs3-devel
%else
BuildRequires:	kdelibs-devel
%endif
BuildRequires:	libjpeg-devel


%description
KreetingKard is a tool for making Japanese greeting cards. It allows you to 
make greeting cards easily by choosing a template and changing the words.


%prep
%setup -q
%patch0 -p1 -b .gcc41

sed -i -e 's|grep klineedit|grep -i klineedit|' configure

%build
%configure

# Don't call autoheader
touch config.h.in config.h
# Remove rpath
for f in `find . -name Makefile` ; do
	%{__sed} -i.rpath -e 's|^\([A-Z][A-Z]*_RPATH = \).*|\1|' $f
done

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="%{__install} -c -p"

# Fixing up
# 1. Desktop file treatment
%{__sed} -i -e '/^Pattern/d' \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--add-category Office \
%if 0%{?fedora} < 19
	--vendor fedora \
%endif
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/applnk/

# 2 KDE common symlink to relative
unlink $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common
%{__ln_s} -f '../common' $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common

# 3 Install icons
for s in 16 32 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	%{__install} -cp -m 644 src/cr${s}-app-%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

# 4. gettext .mo file
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%doc	COPYING
%doc	README

%{_bindir}/%{name}

%{_datadir}/apps/%{name}/
%{_datadir}/icons/crystalsvg/??x??/*/*.png
%{_datadir}/mimelnk/application/x-%{name}.desktop

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png

%{_defaultdocdir}/HTML/en/%{name}/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-8
- Fix for UIC plugin detection behavior change

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-7.1
- Remove obsolete scriptlets

* Wed Aug  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-7
- Add BR: libjpeg-devel explicitly

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.1-6.4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-6
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.1-5
- F-17: rebuild against gcc47

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-3
- GTK icon cache updating script update

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Mon Oct 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-2
- Fix typo.

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- Initial spec file
