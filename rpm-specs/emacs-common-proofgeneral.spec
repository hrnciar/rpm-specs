%global pkg         proofgeneral
%global commit      ea62543527e6c0fcca8bbb70695e25c2f5d89614
%global date        20200506
%global forgeurl    https://github.com/ProofGeneral/PG

Name:           emacs-common-%{pkg}
Version:        4.4

%forgemeta

Release:        11%{?dist}
Summary:        Emacs mode for standard interaction interface for proof assistants

License:        GPLv2
URL:            https://proofgeneral.github.io/
Source0:        %{forgesource}
Source1:        %{pkg}.appdata.xml
# Backwards compatibility shell script launcher
Source2:        %{pkg}
# Additional icon sizes created with gimp from icons in the source file
Source3:        %{pkg}-96x96.png
Source4:        %{pkg}-256x256.png

# Patch 0 - Fedora specific, don't do an "install-info" in the make process
# (which would occur at build time), but instead put it into a scriptlet
Patch0:         pg-4.2-Makefile.patch

# Bring the desktop file up to date with current standards.
Patch1:         pg-4.2-desktop.patch

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  emacs
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  tex-cm-super
BuildRequires:  tex-ec
BuildRequires:  texinfo-tex

Requires:       hicolor-icon-theme

Recommends:     prooftree

%description
Proof General is a generic front-end for proof assistants (also known
as interactive theorem provers) based on Emacs.

Proof General allows one to edit and submit a proof script to a proof
assistant in an interactive manner:
- It tracks the goal state, and the script as it is submitted, and
  allows for easy backtracking and block execution.
- It adds toolbars and menus to Emacs for easy access to proof
  assistant features.
- It integrates with Emacs Unicode support for some provers to provide
  output using proper mathematical symbols.
- It includes utilities for generating Emacs tags for proof scripts,
  allowing for easy navigation.

Proof General supports a number of different proof assistants
(Isabelle, Coq, PhoX, and LEGO to name a few) and is designed to be
easily extendable to work with others.

%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run Proof General under GNU Emacs
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

# This can be removed when Fedora 33 reaches EOL
Obsoletes:      emacs-%{pkg}-el < 4.4-11
Provides:       emacs-%{pkg}-el = %{version}-%{release}

%description -n emacs-%{pkg}
Proof General is a generic front-end for proof assistants based on Emacs.

This package contains the byte compiled elisp packages to run Proof
General with GNU Emacs.

%prep
%forgesetup
%patch0
%patch1

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix rpmlint complaints:

# Correct permissions for isartags script
chmod 755 isar/isartags
# Remove .cvsignore files
find . -name .cvsignore -delete

# Fix non UTF-8 documentation and theory files
for f in phox/sqrt2.phx; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf8 $f.orig > $f
  fixtimestamp $f
done

# Fix script interpreter for the isar interface
sed -i.orig 's,/usr/bin/env bash,/bin/bash,' isar/interface
fixtimestamp isar/interface
chmod 755 isar/interface

%build
# Make full copies of emacs versions, set options in the proofgeneral start
# script
make clean
make EMACS=emacs compile bashscripts perlscripts doc

%install
%define full_doc_dir %{_datadir}/doc/%{pkg}
%define full_man_dir %{_mandir}/man1

%define doc_options DOCDIR=%{buildroot}%{full_doc_dir} MANDIR=%{buildroot}%{full_man_dir} INFODIR=%{buildroot}%{_infodir}
%define common_options PREFIX=%{buildroot}%{_prefix} DEST_PREFIX=%{_prefix} DESKTOP=%{buildroot}%{_datadir} BINDIR=%{buildroot}%{_bindir} %{doc_options}

%define emacs_options ELISP_START=%{buildroot}%{_emacs_sitestartdir} ELISP=%{buildroot}%{_emacs_sitelispdir}/%{pkg} DEST_ELISP=%{_emacs_sitelispdir}/%{pkg}

make EMACS=emacs %{common_options} %{emacs_options} install install-doc

# Remove empty, obsolete directories
rmdir %{buildroot}%{full_doc_dir}/lclam %{buildroot}%{full_doc_dir}/plastic

# Do not install the INSTALL or COPYING files
rm %{buildroot}%{full_doc_dir}/{COPYING,INSTALL}

# Validate the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/proofgeneral.desktop

# Install the AppData file
# The Packaging Guidelines say we have to run appstram-util validate-relax, but
# the tool is erroring out, claiming that the screenshot URLs are invalid.  I
# have verified that they are valid with both a web browser and wget.  Some of
# them are http and some https; both fail.  No redirects are involved.  I don't
# know what is wrong with appstream-util, but until it stops causing bogus
# failures, I am turning it off.
# appstream-util validate-relax %%{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

# Install the backwards compatibility launcher
cp -p %{SOURCE2} %{buildroot}%{_bindir}

# Install additional icon sizes
install -Dpm 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{pkg}.png
install -Dpm 644 %{SOURCE4} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{pkg}.png

%files
%license COPYING
%{full_doc_dir}
%{full_man_dir}/*
%{_infodir}/*
%{_bindir}/*
%{_datadir}/appdata/%{pkg}.appdata.xml
%{_datadir}/application-registry/%{pkg}.applications
%{_datadir}/applications/%{pkg}.desktop
%{_datadir}/icons/hicolor/*/apps/%{pkg}.png
%{_datadir}/mime-info/%{pkg}.*

%files -n emacs-%{pkg}
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{pkg}/

%changelog
* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 4.4-11.20200506gitea62543
- May 6 2020 git snapshot so emacs-mmm dependency can be dropped (bz 1837683)
- Remove the -el subpackage as required by current package guidelines

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 4.4-6
- Install additional icon sizes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.4-4
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Jerry James <loganjerry@gmail.com> - 4.4-1
- New upstream release
- New project URLs
- Update the AppData file and validate it on installation
- Use the license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Jerry James <loganjerry@gmail.com> - 4.2-2
- Add AppData file

* Sat Aug 24 2013 Jerry James <loganjerry@gmail.com> - 4.2-1
- New upstream release (fixes bz 972343)
- Fix eps2pdf BR (bz 913972 and 992196)
- Add BRs for newer versions of texlive
- Drop upstreamed -elisp patch
- Add upstream workaround for Emacs 24.3 byte-compilation error

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Jerry James <loganjerry@gmail.com> - 4.1-1
- New upstream release
- Upstream no longer supports XEmacs
- Upstream no longer bundles X-Symbol
- Remove unnecessary spec file elements (defattr, etc.)
- Move desktop files into places where they will be used

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 29 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-4
- Incorporated comments from Jerry James about applying his patch:
  patch now applied unconditionally (regardless of Fedora version
  which was used as a somewhat imperfect way to control XEmacs
  version).
- Patch descriptions moved upward in spec file in accordance with
  examples in guidelines.

* Thu Jul 09 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-3
- Added xemacs patch that fixes compilation problems for X-Symbol code.

* Thu Jul 02 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-2
- Excluded bundled X-symbol, mmm-mode.
- Changed requires for these bundled packages.

* Tue Apr 07 2009 Alan Dunn <amdunn@gmail.com> 3.7.1-1
- Initial Fedora RPM.
