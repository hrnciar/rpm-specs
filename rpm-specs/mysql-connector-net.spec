%global debug_package %{nil}

Name:           mysql-connector-net
Version:        6.9.9
Release:        11%{?dist}
Summary:        Mono ADO.NET driver for MySQL

# The entire source code is GPLv2 except Source/MySql.Data/zlib/ which is BSD
License:        GPLv2 and BSD
URL:            http://dev.mysql.com/downloads/connector/net/
Source0:        http://cdn.mysql.com/Downloads/Connector-Net/%{name}-%{version}-src.zip
Source1:        mysql-connector-net.pc

BuildRequires:  mono-devel >= 4.0

Requires:       mono-data >= 4.0
# Mono only available on these:
ExclusiveArch: %{mono_arches}

%description
Connector/Net is a fully-managed ADO.NET driver for MySQL.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for %{name}.

%prep
%setup -q -c
#Avoid sign the assembly due problem with the key
sed -i '77i#if DEBUG' Source/MySql.Data/Properties/AssemblyInfo.cs
sed -i '80i#endif' Source/MySql.Data/Properties/AssemblyInfo.cs
sed -i '81i[assembly: AssemblyKeyName("ConnectorNet")]' Source/MySql.Data/Properties/AssemblyInfo.cs

%build
xbuild /property:Configuration=Release /property:VisualStudioVersion=11.0 Source/MySql.Data/MySql.Data.csproj

%install
%{__mkdir_p} %{buildroot}/%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}/%{_monogacdir}/
%{__mkdir_p} %{buildroot}/%{_monodir}/mysql-connector-net/

install -p -m0644 %SOURCE1 %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 Source/MySql.Data/bin/v4.5/Release/MySql.Data.dll %{buildroot}%{_monodir}/mysql-connector-net/

gacutil -i %{buildroot}%{_monodir}/mysql-connector-net/MySql.Data.dll -f -package mysql-connector-net -root %{buildroot}/%{_prefix}/lib

%files
%doc CHANGES README
%license COPYING
%{_monogacdir}/*
%dir %{_monodir}/mysql-connector-net
%{_monodir}/mysql-connector-net/*

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9.9-2
- mono rebuild for aarch64 support

* Mon Jul 04 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.9-1
- Update to 6.9.9
- Avoid sign the assembly due problem with the key

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 6.9.8-1
- Update to 6.9.8 (#1273674)

* Mon Oct 12 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.7-1
- Update to 6.9.7
- Use xbuild property parameter to build for mono 4

* Thu Jul 30 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.6-4
- Own directory mysql-connector-net
- Remove define for EPEL
- Fix license

* Mon May 18 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.6-3
- Use global insted define

* Wed Apr 22 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.6-2
- Add pc file
- Fix build for mono

* Thu Nov 21 2013 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.9.6-1
- Initial packaging
