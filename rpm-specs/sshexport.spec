# The obsoleted package was named this.
%global oldpkg ssh-installkeys

# Simplify the logic to choose the right Python version
# for older distributions.
%if 0%{?fedora} || 0%{?rhel} >= 8
%global python_prg %{__python3}
%global python_ver python3
%else
%global python_prg %{__python2}
%global python_ver python2
%endif


Name:           sshexport
Version:        2.4
Release:        3%{?dist}
Summary:        Install your SSH keys on remote sites

# Bundled pexpect is ISC licensed.  The license text
# is preserved inside of the Python script.
License:        BSD and ISC
URL:            http://www.catb.org/~esr/%{name}
Source0:        %{url}/%{name}-%{version}.tar.gz

# Upstreamable patch to fix a minor error in the manpage.
Patch0000:      %{name}-2.4-fix_manpage.patch

# The final package can savely be architecture-independent, as
# there are no c-compiled binaries.  Just a Python script.
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  %{python_ver}-devel
BuildRequires:  xmlto

# There has never been a 1.10 release, so we use this version
# for the obsoletion of the old package.  We also provide an
# alias to the old package name with the recent VR.
Obsoletes:      %{oldpkg} < 1.10
Provides:       %{oldpkg} = %{version}-%{release}

# This bundles pexpect.
Provides:       bundled(%{python_ver}-pexpect) = 2.3

%description
This script tries to export SSH public keys to specified sites.
It will walk the user through generating key pairs if it doesn't
find any to export.  It handles all the fiddly details, like
remembering the SSH key file names, updating the authorized_keys
and making sure local and remote permissions are correct.
It tells you what it's doing if it has to change anything.


%prep
%autosetup -p 1

# Remove possible prebuilt stuff.
rm -f %{name}.{1,html}


%build
# We just need to build the documentation using the Makefile.
%make_build %{name}.{1,html}

# Use a versioned Python interpreter to get the correct
# autogenerated runtime requirements.
# Also preserve the timestamp of the original file.
sed 's~^#!.*~#!%{python_prg}~1' < %{name} > %{name}.fix
touch -r %{name}{,.fix}
mv -f %{name}{.fix,}


%install
# Install the files to their final locations manually,
# as we do not have a working install target in the Makefile.
install -Dpm 0755 {,%{buildroot}%{_bindir}/}%{name}
install -Dpm 0644 {,%{buildroot}%{_mandir}/man1/}%{name}.1

# Compatibility links for the old executable script,
# as the new script is fully cli compatible.
ln -s %{name} %{buildroot}%{_bindir}/%{oldpkg}
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/%{oldpkg}.1


%files
%doc README %{name}.html
%license COPYING
# Files need to be listed individually, as older versions
# of rpmbuild do not support bash expansions here.
%{_bindir}/%{name}
%{_bindir}/%{oldpkg}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{oldpkg}.1*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-1
- Rename ssh-installkeys to sshexport (#1728828)

* Fri Jul 12 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-0.5
- Add actual Python version to bundled Provides

* Thu Jul 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-0.4
- Add Provides and licensing clarification for bundled pexpect

* Wed Jul 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-0.3
- Add a small patch to fix the generated manpage

* Wed Jul 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-0.2
- Small spec file improvements, added verbose comments

* Wed Jul 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.4-0.1
- Initial rpm release (#1728828)
