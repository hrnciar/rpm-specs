# These is the exact upstream version we are packaging
%global ver_maj 2
%global ver_min 13
%global ver_patch 16

# All Unison versions sharing ver_compat are compatible
# Examples are 2.13.15 and 2.13.16 -> ver_compat == 2.13
# In older versions, even patch levels were not compatible
# Examples are ver_compat==2.9.0 and ver_compat==2.9.1
%global ver_compat      %{ver_maj}.%{ver_min}
%global ver_compat_name %{ver_maj}%{ver_min}
%global ver_noncompat   .%{ver_patch}

# ver_priority is the first component of ver_compat, catenated with the second
# component of ver_compat zero-filled to 3 digits, catenated with a final
# zero-filled 3-digit field. The final field contains the 3rd component of
# ver_compat (if there is one), otherwise 0.
%global ver_priority %(printf %%d%%03d%%03d `echo %{ver_compat}|sed 's/\\./ /g'`)

# Is this package the unisonNNN package with the highest ${ver_compat}
# available in this Fedora branch/release? If so, we provide unison.
%global provide_unison 0

Name:      unison%{ver_compat_name}
Version:   %{ver_compat}%{ver_noncompat}
Release:   39%{?dist}

Summary:   Multi-master File synchronization tool

License:   GPL+
URL:       http://www.cis.upenn.edu/~bcpierce/unison
Source0:   http://www.cis.upenn.edu/~bcpierce/unison/download/releases/unison-%{version}/unison-%{version}.tar.gz
Source1:   unison.png

# Fix for OCaml 3.12.
Patch1:    unison213-ocaml312.patch
# Small hack to get it working with newer lablgtk.
Patch2:    unison213-gtk.patch
# Various changes for OCaml 4.08.
Patch3:    unison213-ocaml408.patch

BuildRequires: ocaml >= 3.10.2-2
BuildRequires: ocaml-lablgtk-devel >= 2.6.0
BuildRequires: tetex-latex
BuildRequires: desktop-file-utils
# for lablgtk
BuildRequires: gtk2-devel

Requires:            xorg-x11-fonts-misc
Requires(posttrans): %{_sbindir}/alternatives
Requires(postun):    %{_sbindir}/alternatives

# Enforce the switch from unison to unisonN.NN
Obsoletes: unison < 2.27.57-3
# Let users just install "unison" if they want
%if 0%{?provide_unison}
Provides: unison = %{version}-%{release}
%endif

%description
Unison is a multi-master file-synchronization tool. It allows two
replicas of a collection of files and directories to be stored on
different hosts (or different locations on the same host), modified
separately, and then brought up to date by propagating the changes
in each replica to the other.

Note that this package contains Unison version %{ver_compat}, and
will never be upgraded to a different major version. Other packages
exist if you require a different major version.

%prep
%setup -q -n unison-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make NATIVE=true UISTYLE=gtk2 OCAMLOPT="ocamlopt -unsafe-string -g"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -f unison %{buildroot}%{_bindir}/unison-%{ver_compat}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -f %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/unison-%{ver_compat}.png

cat > unison-%{ver_compat}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=unison-%{ver_compat}
Name=Unison File Synchronizer (version %{ver_compat})
GenericName=File Synchronizer
Comment=Multi-master File synchronization tool
Terminal=false
Icon=unison-%{ver_compat}
Encoding=UTF-8
StartupNotify=true
EOF

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
%endif
    --add-category Application \
    --add-category Utility \
    --dir %{buildroot}%{_datadir}/applications \
    unison-%{ver_compat}.desktop

%posttrans
alternatives \
  --install \
  %{_bindir}/unison \
  unison \
  %{_bindir}/unison-%{ver_compat} \
  %{ver_priority}

# Clean up after previous package version's incorrect alternatives usage.
alternatives --remove unison-icon \
  %{_datadir}/pixmaps/unison-%{ver_compat}.png || :
alternatives --remove unison-desktop \
  %{_datadir}/applications/fedora-unison-%{ver_compat}.desktop || :

%postun
if [ $1 -eq 0 ]; then
  alternatives --remove unison \
    %{_bindir}/unison-%{ver_compat}
fi
exit 0

%files
%doc COPYING NEWS README
%attr(0755, root, root) %{_bindir}/unison-%{ver_compat}
%{_datadir}/applications/*unison-%{ver_compat}.desktop
%{_datadir}/pixmaps/unison-%{ver_compat}.png

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard W.M. Jones <rjones@redhat.com> - 2.13.16-35
- Use unsafe-strings with OCaml 4.06.
- Small hack to keep it working with new lablgtk.
- Fix date in changelog.
- Enable debugging.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 2.13.16-30
- remove ExcludeArch

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 2.13.16-29
- Rebuild for OCaml 4.04.0.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.16-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.13.16-27
- Use global instead of define.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.13.16-22
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Richard W.M. Jones <rjones@redhat.com> - 2.13.16-20
- Rebuild for OCaml 4.00.1.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Richard W.M. Jones <rjones@redhat.com> - 2.13.16-18
- Include fix for OCaml 3.12.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 8 2009 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-13
- Add Requires: xorg-x11-fonts-misc

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 2.13.16-12
- Rebuild for OCaml 3.11.0+rc1.

* Mon May 26 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-11
- Rebuild with OCaml 3.10.2-2 (fixes bz 441685, 445545).

* Sun Mar 30 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-10
- Don't use alternatives for desktop and icon files, to avoid duplicate
  menu entries.

* Wed Mar 19 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-9
- Fix license to match correct interpretation of source & GPL
- Remove Excludes for ppc64, since ocaml is available there now, in devel

* Sat Mar 15 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-8
- Rename package unison2.13 -> unison213 to match Fedora naming rules
- Automatically calculate ver_priority using the shell; easier maintenance

* Sat Mar 1 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-7
- Use Provides/Obsoletes to provide upgrade path, per:
  http://fedoraproject.org/wiki/Packaging/NamingGuidelines

* Thu Feb 28 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-6
- Explicitly conflict with existing unison package

* Fri Feb 22 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-5
- Use alternatives to provide /usr/bin/unison, and other cleanups

* Thu Feb 21 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2.13.16-4
- Create 2.13 compatibility package

* Tue Aug 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-3
- Rebuild for FE6

* Tue Feb 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-2
- Rebuild for Fedora Extras 5

* Thu Sep  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.13.16-1
- New Version 2.13.16

* Sun Jul 31 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.12.0-0
- New Version 2.12.0

* Fri May 27 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.10.2-7
- Bump and rebuild with new ocaml and new lablgtk

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.10.2-6
- rebuild on all arches

* Mon May 16 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.10.2-5
- Patch: http://groups.yahoo.com/group/unison-users/message/3200

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 24 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:2.10.2-2
- BR gtk2-devel
- Added NEWS and README docs

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.10.2-1
- New Version 2.10.2

* Wed Apr 28 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.74-0.fdr.1
- New Version 2.9.74
- Added icon

* Tue Jan 13 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.72-0.fdr.1
- New Version 2.9.72

* Tue Dec  9 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.70-0.fdr.2
- Changed Summary
- Added .desktop file

* Fri Oct 31 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.9.70-0.fdr.1
- First Fedora release
