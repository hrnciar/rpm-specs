Name:           nvi
Version:        1.81.6
Release:        24%{?dist}
Summary:		4.4BSD re-implementation of vi

License:        BSD
URL:            http://www.bostic.com/vi/
Source0:		http://www.kotnet.org/~skimo/%{name}/devel/%{name}-%{version}.tar.bz2
Patch1:         nvi-01-additional_upstream_data.patch
Patch2:         nvi-03-db4.patch
Patch3:         nvi-04-confdefs.patch
Patch4:         nvi-06-default_value_escapetime.patch
Patch5:         nvi-07-flush_cache.patch
Patch6:         nvi-08-lfs.patch
Patch7:         nvi-08-safe_printf.patch
Patch8:         nvi-08-tempfile_umask.patch
Patch9:         nvi-09-casting.patch
Patch10:        nvi-10-no_one_line_visual.patch
Patch11:        nvi-11-backward_sentence_moving.patch
Patch12:        nvi-12-horiz_scroll_count.patch
Patch13:        nvi-13-widechar_horrors.patch
Patch14:        nvi-14-private_regex_fixes.patch
Patch15:        nvi-15-search_word.patch
Patch16:        nvi-16-manpage_errors.patch
Patch17:        nvi-17-tutorial_typos.patch
Patch18:        nvi-18-dbpagesize_binpower.patch
Patch19:        nvi-19-include_term_h.patch
Patch20:        nvi-20-glibc_has_grantpt.patch
Patch21:        nvi-21-exrc_writability_check.patch
Patch22:        nvi-23-debian_alternatives.patch
Patch23:        nvi-24-fallback_to_dumb_term.patch
Patch24:        nvi-25-manpage_note_dropped_F.patch
Patch25:        nvi-26-trailing_tab_segv.patch
Patch26:        nvi-27-support_C_locale.patch
Patch27:        nvi-28-regex_widechar.patch
Patch28:        nvi-29-file_backup.patch
Patch29:        nvi-30-autoconf-269-aarch64.patch


BuildRequires:  gcc
BuildRequires:	ncurses-devel, libdb-devel

%description
Vi is the original screen based text editor for Unix systems.
It is considered the standard text editor, and is available on
almost all Unix systems.

Nvi is intended as a "bug-for-bug compatible" clone of the original
BSD vi editor. As such, it doesn't have a lot of snazzy features as do
some of the other vi clones such as elvis and vim. However, if all
you want is vi, this is the one to get.

%prep
%setup -q
%patch1 -p1  -b .additional_upstream_data
%patch2 -p1  -b .db4
%patch3 -p1  -b .confdefs
%patch4 -p1  -b .default_value_escapetime
%patch5 -p1  -b .flush_cache
%patch6 -p1  -b .lfs
%patch7 -p1  -b .safe_printf
%patch8 -p1  -b .tempfile_umask
%patch9 -p1  -b .casting
%patch10 -p1 -b .no_one_line_visual
%patch11 -p1 -b .backward_sentence_moving
%patch12 -p1 -b .horiz_scroll_count
%patch13 -p1 -b .widechar_horrors
%patch14 -p1 -b .private_regex_fixes
%patch15 -p1 -b .search_word
%patch16 -p1 -b .manpage_errors
%patch17 -p1 -b .tutorial_typos
%patch18 -p1 -b .dbpagesize_binpower
%patch19 -p1 -b .include_term_h
%patch20 -p1 -b .glibc_has_grantpt
%patch21 -p1 -b .exrc_writability_check
%patch22 -p1 -b .debian_alternatives
%patch23 -p1 -b .fallback_to_dumb_term
%patch24 -p1 -b .manpage_note_dropped_F
%patch25 -p1 -b .trailing_tab_segv
%patch26 -p1 -b .support_C_locale
#patch27 -p1 -b .regex_widechar.patch
%patch28 -p1 -b .file_backup
%patch29 -p1 -b .autoconf269


%build
cp -f /usr/lib/rpm/config.{guess,sub} dist/
(cd build.unix && \
  OPTFLAG="$RPM_OPT_FLAGS" \
  ac_cv_path_vi_cv_path_sendmail=/usr/sbin/sendmail \
  vi_cv_revoke=no \
  ../dist/configure \
	--disable-curses \
	--prefix=%{_prefix} \
	--disable-shared --enable-static \
	--enable-widechar \
	--disable-threads \
	--without-x \
	--with-gnu-ld=yes \
	--datadir='%{_datadir}' \
	--mandir='%{_mandir}' \
	--program-prefix=n
)
sed -i -e '/define.*_PATH_MSGCAT/ s/".*"/"\/usr\/share\/vi\/catalog\/"/' \
    build.unix/pathnames.h
make -C build.unix %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make -C build.unix install prefix=%{_prefix} DESTDIR=$RPM_BUILD_ROOT 
find $RPM_BUILD_ROOT \( -name \*.a -o -name \*.la \) -delete
mv $RPM_BUILD_ROOT%{_datadir}/{vi,nvi}
mv $RPM_BUILD_ROOT%{_datadir}/nvi/recover \
    $RPM_BUILD_ROOT%{_bindir}/nvi.recover 
chmod 775 $RPM_BUILD_ROOT%{_bindir}/nvi.recover



%files
%doc LICENSE README* TODO
%{_mandir}/*/*
%{_datadir}/nvi/
%{_bindir}/nex
%{_bindir}/nvi
%{_bindir}/nview
%{_bindir}/nvi.recover

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.81.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 09 2014 Karsten Hopp <karsten@redhat.com> 1.81.6-12
- use uptodate config.guess and config.sub to be able to build on ppc64le

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 25 2013 Matěj Cepl <mcepl@redhat.com> - 1.81.6-9
- Apply patch by Dennis Gilmore (bug#926255)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.81.6-6
- Change BR: db4-devel to libdb-devel

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 24 2010 Matěj Cepl <mcepl@redhat.com> - 1.81.6-2
- Fixing review comments

* Tue Jun 22 2010 Matěj Cepl <mcepl@redhat.com> - 1.81.6-1
- Initial experimental package
