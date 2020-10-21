# Package needs to stay arch specific (due to nagios plugins location), but
# there's nothing to extract debuginfo from
%global debug_package %{nil}

%define nagios_plugins_dir %{_prefix}/lib64/nagios/plugins

Name:       nagios-plugins-fts
Version:    3.6.0
Release:    5%{?dist}
Summary:    Nagios probes to be run remotely against FTS3 machines
License:    ASL 2.0
URL:        http://fts3-service.web.cern.ch/
# following commands to generate the tarball:
#  git clone https://gitlab.cern.ch/fts/nagios-plugins-fts.git -b master --depth=1 nagios-plugins-fts-3.5.0
#  cd nagios-plugins-fts-3.5.0
#  git checkout v3.5.0
#  cd ..
#  tar --exclude-vcs -vczf nagios-plugins-fts-3.5.0.tar.gz nagios-plugins-fts-3.5.0

Source0: %{name}-%{version}.tar.gz
#Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%if %{?fedora}%{!?fedora:0} >= 18 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:  cmake
%else
BuildRequires:  cmake28
%endif

Requires:   nagios%{?_isa}
Requires:   python3%{?_isa}
Requires:   python3-pycurl%{?_isa}

%if 0%{?rhel} && 0%{?rhel} <= 5
Requires:   python-simplejson%{?_isa}
%endif

%description
This package provides the nagios probes for FTS3. Usually they are installed
in the nagios host, and they will contact the remote services running in the
FTS3 machines.

%prep
%setup -qc -n %{name}-%{version}

%build
%if %{?fedora}%{!?fedora:0} >= 18 || %{?rhel}%{!?rhel:0} >= 7
%cmake . -DCMAKE_INSTALL_PREFIX=/
%else
%cmake28 . -DCMAKE_INSTALL_PREFIX=/
%endif

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

make install DESTDIR=%{buildroot}

%files
%config(noreplace) %{_sysconfdir}/nagios/objects/fts3-template.cfg
%{nagios_plugins_dir}/fts
%doc LICENSE README.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Andrea Manzi <amanzi@cern.ch> - 3.6.0-1
- python3 compatible release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Andrea Manzi <amanzi@cern.ch> - 3.5.0-2
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 12 2013 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 3.2.0-1
- Initial build

