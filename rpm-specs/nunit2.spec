%global debug_package %{nil}

Name:           nunit2
Version:        2.6.4
Release:        24%{?dist}
Summary:        Unit test framework for CLI
License:        MIT with advertising
Url:            http://www.nunit.org/
Source0:        https://github.com/nunit/nunitv2/archive/%{version}.tar.gz
Source1:        nunit2.pc
Source2:        nunit2-gui.sh
Source3:        nunit2-console.sh
Source4:        nunit2.desktop
BuildRequires:  mono-devel libgdiplus-devel desktop-file-utils mono-winforms
ExclusiveArch:  %{mono_arches}

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

NUnit targets the CLI (Common Language Infrastructure) and supports Mono and
the Microsoft .NET Framework.

%package gui
Summary:        Tools for run NUnit test
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mono-winforms

%description gui
Desktop application for run NUnit test

%package doc
Summary:        Documentation package for NUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for NUnit

%package        devel
Summary:        Development files for NUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for %{name}.

%prep
%setup -qn nunitv2-%{version}

%build

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%{?exp_env}
%{?env_options}
xbuild /property:Configuration=Debug ./src/NUnitCore/core/nunit.core.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitCore/interfaces/nunit.core.interfaces.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitFramework/framework/nunit.framework.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitMocks/mocks/nunit.mocks.csproj
xbuild /property:Configuration=Debug ./src/ClientUtilities/util/nunit.util.dll.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console/nunit-console.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console-exe/nunit-console.exe.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui/nunit-gui.csproj
xbuild /property:Configuration=Debug ./src/GuiComponents/UiKit/nunit.uikit.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiException/UiException/nunit.uiexception.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui-exe/nunit-gui.exe.csproj

%install
%{?env_options}
mkdir -p %{buildroot}%{_monodir}/nunit2
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/NUnit2
install -p -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig
install -p -m0755 %{SOURCE2} %{buildroot}%{_bindir}/nunit-gui26
install -p -m0755 %{SOURCE3} %{buildroot}%{_bindir}/nunit-console26
install -p -m0644 src/ConsoleRunner/nunit-console-exe/App.config %{buildroot}%{_monodir}/nunit2/nunit-console.exe.config
install -p -m0644 src/GuiRunner/nunit-gui-exe/App.config %{buildroot}%{_monodir}/nunit2/nunit.exe.config
find %{_builddir}/%{?buildsubdir}/bin -name \*.dll -exec install \-p \-m0755 "{}" "%{buildroot}%{_monodir}/nunit2/" \;
find %{_builddir}/%{?buildsubdir}/bin -name \*.exe -exec install \-p \-m0755 "{}" "%{buildroot}%{_monodir}/nunit2/" \;
for i in nunit-console-runner.dll nunit.core.dll nunit.core.interfaces.dll nunit.framework.dll nunit.mocks.dll nunit.util.dll ; do
    gacutil -i %{buildroot}%{_monodir}/nunit2/$i -package nunit2 -root %{buildroot}%{_monodir}/../
done
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE4}
cp -p src/GuiRunner/nunit-gui-exe/App.ico %{buildroot}/%{_datadir}/icons/NUnit2/nunit.ico

%files
%license license.txt
%{_bindir}/nunit-console*
%dir %{_monodir}/nunit2
%{_monodir}/nunit2/nunit-console.exe*
%{_monogacdir}/nunit*
%{_monodir}/nunit2/*.dll

%files gui
%{_bindir}/nunit-gui*
%{_monodir}/nunit2/nunit.exe*
%{_datadir}/applications/nunit2.desktop
%{_datadir}/icons/NUnit2

%files doc
%license doc/license.html
%doc doc/*

%files devel
%{_libdir}/pkgconfig/nunit2.pc

%post gui
/bin/touch --no-create %{_datadir}/icons/NUnit &>/dev/null || :

%postun gui
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/NUnit &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/NUnit &>/dev/null || :
fi

%posttrans gui
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/NUnit &>/dev/null || :

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-23
- Rebuilt with new mono package so that the Provides is fixed again

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-21
- Explicitly require some mono packages because the provides script fail

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 2.6.4-14
- aarch64 bootstrap

* Tue Jul 26 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-13
- rename package to nunit2
- drop references to mono-nunit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.6.4-11
- Replace nunit-runner with nunit-gui with only desktop frontend

* Sun Nov 01 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.6.4-10
- Split runner tool in subpackage

* Tue Aug 04 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-9
- obsoleting mono-nunit and mono-nunit-devel (bug 1247825)

* Fri Jul 17 2015 Dan Horák <dan[at]danny.cz> - 2.6.4-8
- set ExclusiveArch

* Mon Jul 13 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-7
- require desktop-file-utils for building and make sure we own the icons/NUnit directory

* Mon Jul 13 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-5
- fix Requires for devel package, and fixing other issues

* Mon Jul 13 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-2
- include a desktop file and install the icon

* Mon Jun 22 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.4-1
- upgrade to 2.6.4
- fix the license
- fix some rpmlint warnings and errors

* Thu Jun 04 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.3-6
- do not replace mono-nunit. fix some rpmlint warnings and errors

* Wed Jun 03 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.3-5
- Use mono macros
- Require isa in devel subpackage
- Use global insted define

* Tue May 19 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.3-4
- this package replaces mono-nunit

* Mon May 04 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.6.3-3
- Move to 2.6 folder for compat with other versions
- Use real source file

* Tue Apr 21 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.6.3-2
- Split nunit.pc into devel package
- Use upstream zip source
- Add ExclusiveArch

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.3-1
- build with Mono4

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.6.3-0
- copy from Xamarin NUnit spec
