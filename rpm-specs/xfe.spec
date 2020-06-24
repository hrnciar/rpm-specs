%global	hash_thread1	2501673c
%global	hash_thread2	5d70

Name:		xfe
Version:	1.43.2
Release:	3%{?dist}
Summary:	X File Explorer File Manager

License:	GPLv2+
URL:		http://roland65.free.fr/xfe/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Temporarily
# Use system-wide startup-notification: need discuss with upstream
Patch0:	xfe-1.43-use-system-libsn.patch

BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	fox-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrandr-devel
BuildRequires:	startup-notification-devel
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(x11-xcb)
# Patch0
BuildRequires:	autoconf
BuildRequires:	automake

%description
X File Explorer (xfe) is a lightweight file manager for X11, 
written using the FOX toolkit.

%package	theme
Summary:	Extra theme files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	theme
This package contains extra theme files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .syssn

for f in \
	ChangeLog
do
	mv $f{,.iso}
	iconv -f ISO-8859-1 -t UTF-8 -o $f{,.iso}
	touch -r $f{.iso,}
	rm -f $f.iso
done

# Fix libreoffice related command name (bug 1788292)
sed -i.oo xferc.in \
	-e 's|lobase|oobase|g' \
	-e 's|localc|oocalc|g' \
	-e 's|lodraw|oodraw|g' \
	-e 's|loimpress|ooimpress|g' \
	-e 's|lomath|oomath|g' \
	-e 's|lowriter|oowriter|g' \
	%{nil}

# Patch0
autoreconf -fi
rm -rf libsn

%build
%configure \
	--bindir=%{_libexecdir}/%{name}
make %{?_smp_mflags}

%install
%make_install \
	INSTALL="install -p"

%find_lang %{name}

# Tweak too generic and short names
mkdir -p %{buildroot}%{_datadir}/%{name}/pixmaps
mkdir -p %{buildroot}%{_bindir}
for suffix in \
	i e p w
do
	cat > %{buildroot}%{_bindir}/xfe-xf${suffix} <<EOF
#!/bin/sh
export PATH=%{_libexecdir}/%{name}:\$PATH
exec xf${suffix} \$@
EOF
	chmod 0755 %{buildroot}%{_bindir}/xfe-xf${suffix}

	mv %{buildroot}%{_datadir}/pixmaps/xf${suffix}.{png,xpm} \
		%{buildroot}%{_datadir}/%{name}/pixmaps/
	mv %{buildroot}%{_datadir}/applications/{,xfe-}xf${suffix}.desktop
	# Modify desktop file
	sed -i \
		-e "\@^Exec=@s|xf${suffix}|xfe-xf${suffix}|" \
		-e "s|Icon=xf${suffix}|Icon=%{_datadir}/%{name}/pixmaps/xf${suffix}.png|" \
		%{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop
	desktop-file-validate %{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop

	mv %{buildroot}%{_mandir}/man1/{,xfe-}xf${suffix}.1
done
rmdir %{buildroot}%{_datadir}/pixmaps/

# Move configuration files
mkdir %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/xferc \
	%{buildroot}%{_sysconfdir}
ln -sf %{_sysconfdir}/xferc %{buildroot}%{_datadir}/%{name}/xferc

%files	-f %{name}.lang
%doc	AUTHORS
%doc	BUGS
%license	COPYING
%doc	ChangeLog
%doc	README
%doc	TODO

%config(noreplace)	%{_sysconfdir}/xferc

%{_bindir}/xfe-xf*
%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/xf*
%{_datadir}/applications/xfe-xf*.desktop
%dir	%{_datadir}/%{name}
%{_datadir}/%{name}/xferc
%dir	%{_datadir}/%{name}/icons/
# xferc defaults to gnomeblue-theme, so let's use this
%{_datadir}/%{name}/icons/gnome*-theme/
%{_datadir}/%{name}/pixmaps/

%{_mandir}/man1/xfe-xf*.1*

%files	theme
%{_datadir}/%{name}/icons/*-theme/
%exclude	%{_datadir}/%{name}/icons/gnome*-theme/

%changelog
* Wed Jan 29 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.43.2-3
- Fix libreoffice binding (bug 1788292)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.43.2-1
- 1.43.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 25 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.43.1-1
- 1.43.1

* Fri Jul 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.43-1
- 1.43

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.42-1
- 1.42

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.41-1
- 1.41

* Tue Aug 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.40.1-1
- Formal 1.40.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40.1-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.40.1-0.3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.40.1-0.2
- 1.40.1 (prerelease), for hang up issue using UIM

* Tue Jan 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.40-1
- 1.40

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.37-2
- Patch for freetype 2.5.3 header place change

* Mon Dec  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.37-1
- 1.37

* Sun Sep  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.35-1
- 1.35

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.34-2
- Try to use system-wide startup-notification

* Tue Apr 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.34-1
- Initial packaging
