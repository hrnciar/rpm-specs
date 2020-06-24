Name:           indistarter
Version:        2.2.0
Release:        1%{?dist}
Summary:        GUI to start, stop and control an INDI server

License:        GPLv3+
URL:            http://indistarter.sourceforge.net/
# Upstream uses a trailing 'v' in filename.
# The full Source URL is https://github.com/pchev/%%{name}/archive/v%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz


# This patch avoid stripping debuginfo from binary
# Since this is Fedora specific we don't ask upstream to include
Patch100:       indistarter-2.0.0_fix_debuginfo.patch

ExclusiveArch:  %{fpc_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  lazarus
BuildRequires:  libappstream-glib

%description
Indistarter is a user interface to run a INDI server.
You can configure different profile for your astronomical equipment.
The INDI server can be launched locally or remotely on another computer.
In this last case a ssh tunnel is established to allow local client connection.

%prep
%autosetup -p1

#Remove spurious executable bit
chmod -x ./component/synapse/source/lib/*.pas

%build
# Configure script requires non standard parameters
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Doesn't like parallel building so we can't use make macro
make fpcopts="-O1 -gw3 -fPIC"


%install
make install PREFIX=%{buildroot}%{_prefix}

# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license gpl-3.0.txt LICENSE
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/indigui
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/pixmaps/*.png


%changelog
* Fri Feb 21 2020 Mattia Verga <mattia.verga@protonmail.com> 2.2.0-1
- Upgrade to 2.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Mattia Verga <mattia.verga@protonmail.com> 2.1.0-1
- Upgrade to 2.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Mattia Verga <mattia.verga@protonmail.com> 2.0.0-1
- Upgrade to 2.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Mattia Verga <mattia.verga@email.it> 1.3.0-1
- Upgrade to 1.3.0
- Sources moved to github
- Fix wrong date in changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.75svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2.75svn
- Remove obsolete scriptlets

* Sat Nov 25 2017 Mattia Verga <mattia.verga@email.it> 1.0.0-1.75svn
- Upgrade to 1.0.0
- Move appdata files to metainfo dir

* Sun Sep 03 2017 Mattia Verga <mattia.verga@email.it> 0.9.2-1.69svn
- Upgrade to 0.9.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.65svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Mattia Verga <mattia.verga@tiscali.it> 0.9.1-1.65svn
- Upgrade to 0.9.1
- Change FPC compiler options

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2.63svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 13 2017 Mattia Verga <mattia.verga@tiscali.it> 0.9.0-1.63svn
- Upgrade to 0.9.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2.57svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Mattia Verga <mattia.verga@tiscali.it> 0.8.0-1.57svn
- Upgrade to 0.8.0

* Sun Sep 04 2016 Mattia Verga <mattia.verga@tiscali.it> 0.7.1-1.48svn
- Upgrade to 0.7.1

* Tue Aug 16 2016 Mattia Verga <mattia.verga@tiscali.it> 0.6.0-1.39svn
- Upgrade to 0.6.0

* Sun May 22 2016 Mattia Verga <mattia.verga@tiscali.it> 0.5.0-1.35svn
- Upgrade to 0.5.0

* Fri Apr 22 2016 Mattia Verga <mattia.verga@tiscali.it> 0.4.0-1.28svn
- Upgrade to 0.4.0
- Use new fpc_arches macro as ExclusiveArch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4.20151215svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 01 2016 Mattia Verga <mattia.verga@tiscali.it> 0.3.0-3.20151215svn
- Set fpc options from make command instead of patching sources

* Sun Dec 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-2.20151215svn
- Set ExcludeArch properly

* Tue Dec 15 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.3.0-1.20151215svn
- Update to 0.3.0

* Sat Dec 12 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.2.0-5.20151211svn
- Set ExcludeArch where fpc and lazarus are not available

* Fri Dec 11 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.2.0-4.20151211svn
- Update svn version to fix missing license and appdata

* Wed Dec 09 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.2.0-3.20151203svn
- Added missing license text

* Fri Dec 04 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.2.0-2.20151203svn
- Removed libindi dependency

* Thu Dec 03 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.2.0-1.20151203svn
- Update to 0.2.0 svn
- Added desktop-file-utils to buildrequires
- Removed unneeded ldconfig calls
- Add patch to avoid debuginfo stripping
- Add patch to fix appdata validation

* Fri Jul 31 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.1.0-2.20150623svn
- Fix version/release
- Fix BuildRequires error and files ownership

* Tue Jun 23 2015 Mattia Verga <mattia.verga@tiscali.it> - 0.1.0-1.20150623svn
- Initial release
