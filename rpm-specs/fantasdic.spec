%define		mainver		1.0
%define		betaver		beta7

%if 0%{fedora} < 19
%define		rubyabi		1.9.1
%endif

%define		fedorarel	17


%define		fullrel		%{?betaver:0.}%{fedorarel}%{?betaver:.%betaver}

Name:		fantasdic
Version:	%{mainver}
Release:	%{fullrel}%{?dist}.3
Summary:	Dictionary application using Ruby

License:	GPLv2+
URL:		http://www.gnome.org/projects/fantasdic/
Source0:	http://www.mblondel.org/files/fantasdic/%{name}-%{mainver}%{?betaver:-%betaver}.tar.gz
# ruby-gnome2-Bugs-2865895
# Patch0:	fantasdic-1.0-beta7-workaround-rg2-bg2865895.patch
# Various ruby19 fixes
# Need utf-8 encoding direction
Patch10:	fantasdic-1.0-beta7-ruby19-utf8.patch
# Syntax error fix
Patch11:	fantasdic-1.0-beta7-ruby19-syntax.patch
# Path fix for modules in ruby 19
Patch12:	fantasdic-1.0-beta7-ruby19-pathfix.patch
# Guard sigtrap when calling Gdk::flush (bug 844754, bug 799804)
Patch13:	fantasdic-1.0-beta7-guard-sigtrap.patch
# ::Config was finally renamed to RbConfig in Ruby 2.2.
Patch14:	fantasdic-1.0-beta7-ruby22-rbconfig-fix.patch
# rbpango 3.1.6: use no-gi for now
# pango 1.44.x changed massively: use rbpango gi
Patch15:	fantasdic-1.0-beta7-use-pango-gi.patch

BuildArch:	noarch

%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby 
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby 
%endif

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  ruby-devel

Requires:	ruby
Requires:	rubygem(gettext)

Requires:	ruby(libglade2)
Requires:	ruby(gconf2)
Requires:	ruby(gnome2)
Requires:	ruby(gtk2)
# F-31+: use rbpango-gi
Requires:	rubygem(pango)

Requires(post):		scrollkeeper
Requires(postun):	scrollkeeper

%description
Fantasdic is a dictionary application. It allows to look up words in 
various dictionary sources. It is primarily targetting the GNOME 
desktop but it should work with other platforms, including Windows. 
Fantasdic is Free Software.

%prep
%setup -q -n %{name}-%{mainver}%{?betaver:-%betaver}
#%%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
ln -sf lib vendor_ruby
%patch15 -p4
unlink vendor_ruby

%{__chmod} 0644 tools/*.rb
%{__sed} -i.path -e 's|%{_bindir}/||' fantasdic.desktop

# Fix up documents directory
%{__sed} \
	-i.dir -e '/html/s|%{name}|%{name}-%{mainver}|' \
	lib/fantasdic/ui/browser.rb

%build
export LANG=C.UTF-8

ruby setup.rb config \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
%if 0%{fedora} >= 17
	--siterubyver=%{ruby_vendorlibdir} \
%else
	--siteruby=%{ruby_sitelib} \
%endif
%if 0%{?fedora} >= 19
	--datadir=%{_datadir} \
%endif
	--without-scrollkeeper
ruby setup.rb setup

%install
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

desktop-file-install \
	--add-category 'GTK' \
	--add-category 'Dictionary' \
%if 0%{?fedora} < 19
	--vendor 'fedora' \
%endif
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# hicolor png icon symlinks
target="../../../.."
for n in 16 22 24 32 48
	do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
	%{__ln_s} -f \
		${target}/%{name}/icons/%{name}_${n}x${n}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps/%{name}.png
done

# symlink check
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
pushd $target
if [ "x$(pwd)" != "x$RPM_BUILD_ROOT%{_datadir}" ] ; then
	echo "Possibly symlink broken"
	exit 1
fi
popd
popd

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%{__ln_s} -f ${target}/%{name}/icons/%{name}.svg \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/


# Clean up documents
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/

%{find_lang} %{name}


%check
# Need X, disabling
exit 0
ruby setup.rb test

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name}
exit 0

%postun
scrollkeeper-update -q
[ $1 -eq 0 ] || exit 0
exit 0

%files	-f %{name}.lang 
%defattr(-,root,root,-)
%doc	AUTHORS
%doc	COPY*
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	THANKS
%doc	TODO

%doc	tools/
%doc	data/doc/fantasdic/html/

%{_bindir}/%{name}

%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%{_mandir}/man1/%{name}.1*

%if 0%{fedora} >= 17
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}/
%else
%{ruby_sitelib}/%{name}.rb
%{ruby_sitelib}/%{name}/
%endif



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.17.beta7
- F-31+: use rbpango-gi because of pango 1.44 change

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-0.16.beta7.5
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-0.16.beta7.2
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.16.beta7
- F-26+: use no-gi for pango 3.1.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 1.0-0.15.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.15.beta7
- Fix DATADIR and installation path

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.14.beta7
- F-19: rebuild for ruby 2.0

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.13-beta7
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Aug  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-0.12.beta7
- Guard sigtrap when calling Gdk::flush (bug 844754, bug 799804)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May  3 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-0.11.beta7
- Patch to work with ruby 1.9 (bug 817855)

* Mon Feb 27 2012 Vít Ondruch <vondruch@redhat.com> - 1.0-0.10.beta7
- Fix Gettext dependency.

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.9.beta7
- Rebuilt for Ruby 1.9.3.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.8.beta7
- Revert the last change; fixed in ruby-gnome2 side

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.7.beta7
- Add workaround for ruby-gnome2-Bugs-2865895

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.6.beta7
- F-12: Mass rebuild

* Sun Mar 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.5.beta7
- Remove previous modification for bindtextdomain()
  Fixed on rubygem-gettext side (rubygem-gettext bug 24947, GNOME bug 576826)

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.4.beta7
- 1.0 beta 7
- Fix arguments of bindtextdomain() for ruby(gettext) 2.0.0

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.3.beta6
- GTK icon cache updating script update

* Wed Sep 10 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.2.beta6
- 1.0 beta6

* Sun Jan 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.1.beta5
- Initial packaging


