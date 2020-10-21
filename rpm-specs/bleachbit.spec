Name:       bleachbit
Summary:    Remove sensitive data and free up disk space
URL:        https://www.bleachbit.org/
Version:    4.0.0
Release:    3%{?dist}
License:    GPLv3+ and MIT
BuildArch:  noarch

# Development and bug reports mostly seem to happen BleachBit's GitHub project, but their documentation points to SourceForge for the GPG public key and signatures, so that's where we'll need to get the source tarballs -- https://docs.bleachbit.org/doc/install-on-linux.html#digital-signatures
#Source0: https://github.com/%%{name}/%%{name}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0: https://svwh.dl.sourceforge.net/project/bleachbit/bleachbit/%{version}/bleachbit-%{version}.tar.gz
Source1: https://svwh.dl.sourceforge.net/project/bleachbit/bleachbit/%{version}/detached_signatures/bleachbit-%{version}.tar.gz.sig
Source2: https://svwh.dl.sourceforge.net/project/bleachbit/public_key/andrew2019.key

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if 0%{?rhel}  &&  0%{?rhel} < 8
BuildRequires: python3-rpm-macros
%endif

Requires: gtk3
Requires: python3-chardet
Requires: python3-gobject

%description
Delete traces of your computer activity and other junk files to free
disk space and maintain privacy.

With BleachBit, you can free cache, delete cookies, clear Internet
history, shred temporary files, delete logs, and discard junk you didn't
know was there. Designed for Linux and Windows systems, it wipes clean
thousands of applications including Firefox, Internet Explorer, Adobe
Flash, Google Chrome, Opera, Safari, and many more. Beyond simply
deleting files, BleachBit includes advanced features such as shredding
files to prevent recovery, wiping free disk space to hide traces of
files deleted by other applications, and cleaning Web browser profiles
to make them run faster.



%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q


# Disable update notifications, since package will be updated by DNF or Packagekit.
sed 's/online_update_notification_enabled = True/online_update_notification_enabled = False/g'  --in-place ./bleachbit/__init__.py

# These get installed to %%{_datadir} as non-executable files, and so shouldn't need a shebang at all.
find ./bleachbit/  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/.+$||g' --in-place '{}' +

# Replace any remaining env shebangs, or shebangs calling unversioned or unnecessarily specifically versioned Python, with plain python3.
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/env python3?$|#!%{_bindir}/python3|g' --in-place '{}' +
find ./  -type f  -iname '*.py'  -exec sed --regexp-extended '1s|^#! ?/usr/bin/python[[:digit:][:punct:]]*$|#!%{_bindir}/python3|g' --in-place '{}' +



%build
%py3_build
%make_build --directory ./po/

# Remove Windows-specific functionality.
%make_build delete_windows_files



%install
%make_install  PYTHON=%{__python3}  prefix=%{_prefix}  INSTALL="%{_bindir}/install -Dp"
%make_install --directory ./po/  PYTHON=%{__python3}  prefix=%{_prefix}  INSTALL="%{_bindir}/install -Dp"

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/  org.bleachbit.BleachBit.desktop
install -Dp  org.bleachbit.BleachBit.metainfo.xml  %{buildroot}/%{_metainfodir}/

# "BleachBit As Administrator" app launcher is broken, so we're not shipping any polkit files for now -- https://github.com/bleachbit/bleachbit/issues/950
rm %{buildroot}/%{_datadir}/polkit-1/actions/org.bleachbit.policy

%find_lang %{name}



%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.bleachbit.BleachBit.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml



%files -f %{name}.lang
%doc  README*  CONTRIBUTING.md
%license COPYING
%{_bindir}/bleachbit
%{_datadir}/bleachbit/
%{_datadir}/applications/org.bleachbit.BleachBit.desktop
%{_metainfodir}/org.bleachbit.BleachBit.metainfo.xml
%{_datadir}/pixmaps/bleachbit.png





%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Andrew Toskin <andrew@tosk.in> - 4.0.0-2
- Finished unretired package.
- GPG-verify source tarball.
- Omit upstream's "BleachBit As Administrator" app launcher, since it's
  broken on Fedora.

* Wed Apr 22 2020 Andrew Toskin <andrew@tosk.in> - 4.0.0-1
- Prepare to unretire package after upstream ported to GTK3 and Python3.
