# Note on building bbdb with support for VM: if support for VM in bbdb is
# required, then the source elisp for VM must be installed at build time. If
# support for BBDB is required in VM, then the BBDB source elisp must be present
# at build time. Hence there is a circular BuildRequires and bootstrapping is
# required. The way to do this is (i) build emacs-vm without BuildRequires:
# emacs-bbdb (ii) build emacs-bbdb with BuildRequires: emacs-vm (iii)
# rebuild emacs-vm with BuildRequires: emacs-bbdb.  Or vice versa.
%define vmsupport 1

%define lispdir %{_emacs_sitelispdir}/bbdb

Name:           emacs-bbdb
Version:        3.1.2
Release:        15%{?dist}
Epoch:          1
Summary:        A contact management utility for use with Emacs
Summary(sv):    Ett verktyg för att hantera kontakter i Emacs

License:        GPLv3+
URL:            http://savannah.nongnu.org/projects/bbdb/

Source0:        http://download.savannah.gnu.org/releases/bbdb/bbdb-%{version}.tar.gz
Source1:	emacs-bbdb.metainfo.xml
Patch0:         bbdb-3.1.2-migrate-fix.patch
Patch1:         bbdb-3.1.2-mh-folder-mode-fix.patch

BuildArch:      noarch
BuildRequires:  emacs info texinfo texinfo-tex
BuildRequires:	libappstream-glib

%if %{vmsupport}
BuildRequires:  emacs-vm
%endif

Requires:       emacs(bin) >= %{_emacs_version}

%description 
BBDB is the Insidious Big Brother Database contact manager for GNU
Emacs.  It provides an address book for email and snail mail
addresses, phone numbers and the like.  It can be linked with various
Emacs mail clients (Message and Mail mode, Rmail, Gnus, MH-E, and VM).
BBDB is fully customizable.

%description -l sv
BBDB är the Insidious Big Brother Database kontakthanterare för GNU
Emacs.  Den tillhandahåller en adressbok för e-post och traditionella
postadresser, telefonnummer och liknande.  Den kan kopplas ihop med
olika Emacs-postklienter (Message- och Mail-läge, Rmail, Gnus, MH-E
och VM).  BBDB går att anpassa fullständigt.


%prep 
%setup -q -n bbdb-%{version}
%patch0 -p1
%patch1 -p1

%build
%if %{vmsupport}
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb --with-vm-dir=%{_emacs_sitelispdir}/vm
%else
%configure --with-lispdir=%{_emacs_sitelispdir}/bbdb
%endif

# Note: make %{?_smp_mflags} fails.
make all

%install
make DESTDIR=%{buildroot} install

# Create and install init file
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cat > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/bbdb-init.el << EOF
(require 'bbdb-loaddefs)
EOF

# Adapt to Fedora-specific naming for doc directory.
mv %{buildroot}%{_docdir}/bbdb %{buildroot}%{_pkgdocdir}

# The COPYING file belongs in the license directory instead.
rm %{buildroot}%{_pkgdocdir}/COPYING

# The install creates a dir file, but this has to be done in package
# installation.
rm %{buildroot}%{_infodir}/dir

# The current documentation is just a template, it doesn't contain any real
# documentation.
rm %{buildroot}%{_infodir}/bbdb.info
rm %{buildroot}%{_pkgdocdir}/bbdb.pdf

# Metainfo
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license COPYING
%{_datadir}/bbdb
%{lispdir}/
%{_pkgdocdir}
%{_emacs_sitestartdir}/bbdb-init.el
%{_datadir}/metainfo/%{name}.metainfo.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Göran Uddeborg <goeran@uddeborg.se> - 1:3.1.2-10
- Metainfo added.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.2-8
- Remove the PDF documentation.  Just like the info file, it is just a
  template (BZ #1457079)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 24 2016 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.2-6
- Remove cleanup code for the info file.  The file was last included in F22,
  and the cleanup is no longer needed in F25 (BZ #1319184)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 26 2015 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.2-3
- Remove the info file.  It currently does not contain any real documentation
  but just a template (BZ #1192873)
- Clean up a warning during RPM build.

* Sun Dec 14 2014 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.2-2
- Allow either 2 and 3 semicolons in databases (BZ #1172912).
- Fix ":" (bbdb-mua-display-sender)  in mh-folder mode (BZ #1172915).
- Update URL to the new Savannah site.
- License is nowdays GPLv3+.
- Include copying license file and a few missing documentation files.

* Mon Jul  7 2014 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.2-1
- Upgrade to new version 3.1.2.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Göran Uddeborg <goeran@uddeborg.se> 1:3.1.1-1
- Upgrade to new major version 3.1.1.
- Update build scriptlets to the new version.
- Remove all patches, they are no longer relevant with the new version.
- Remove obsoletes/provides of -el packages.
- Fix incorrect weekday on earlier changelog record.
- Simplify and shorten the description.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Göran Uddeborg <goeran@uddeborg.se> 1:2.35-11
- Remove undefined default function in menu selection for customizable
  variables.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Göran Uddeborg <goeran@uddeborg.se> 1:2.35-9
- Remove obsolete "clean" and "defattr".
- Update references to the removed -el packages in spec file comments.
- Obsolete -el subpackages strictly less than release 7 rather than
  less than or equal to release 6.  Otherwise release 6 packages with
  a dist tag will be considered newer. (BZ #832822)
- Run bbdb-canonicalize-net-hook manually rather than via
  run-hook-with-args in order to get the desired return value.  (BZ #835318)
- Swedish translation of the summary and description added.

* Tue Jun  5 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:2.35-8
- Change BuildRequires for emacs-vm-el to emacs-vm

* Tue Jun  5 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:2.35-7
- Remove separate emacs-bbdb-el sub-package
- Add patch to work with Emacs 24 (BZ #828582)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 26 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:2.35-4
- Update spec file to use macros installed with the emacs package rather than
  pkgconfig stuff
- Remove BuildRoot and rm -rf buildroot from install section

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov  9 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:2.35-1
- Revert to 2.35 release in order to address BZ 467909 and 467911
- Add bbdb-2.35-fix_lisp_makefile.patch in order to fix build problems
- Add epoch to avoid problems with package updating

* Thu Nov  6 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.36-0.1.20080928cvs
- Rename snapshot to reflect the fact that it is a 2.36 pre-release rather than
  a post 2.35 snapshot
- Fix day of previous spec file changelog entry
- Added a patch to revert upstream SVN revision 106 (which is suitable for
  emacs>=23) (BZ 467909)

* Mon Sep 29 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-9.20080928cvs
- Update to current CVS snapshot, fixing several bugs
- Ensure that bbdb-vm.elc is built and installed (BZ 462875)
- Add --enable-developer to configure for more verbose build info

* Fri Sep 28 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-8
- Correct encoding of ChangeLog and info files
- Correct hash bang in perl scripts which are installed as docs
- correct spelling mistake in description

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-7
- Add init file

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-6
- Add sensible defaults for the case that there is no Emacs
  pkg-config file at build time

* Thu Sep  6 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-5
- Add changes to comply with Emacs add-on packaging guidelines

* Tue May 29 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-4
- Add BuildRequires: emacs-vm-el
- Add macro to determine emacsversion at package build time
- Add Requires emacs-common >= emacsversion
- Add notes about bootstrapping with VM to top of spec file

* Mon May  7 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-3
- Convert info file to correct encoding (Tom Tromey)
- Use install rather than mkdir and cp to install files

* Sat Feb 10 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-2
- Added Requires: tetex, since bbd-print requires TeX to be installed

* Sat Feb  3 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 2.35-1
- Initial package


