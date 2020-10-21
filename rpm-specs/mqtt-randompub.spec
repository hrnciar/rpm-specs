# Created by pyp2rpm-3.3.4
%global pypi_name mqtt-randompub

Name:           %{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Tool for generating MQTT messages on various topics

License:        MIT
URL:            https://github.com/fabaff/mqtt-randompub/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
For testing application and tools which are handling MQTT messages
it's often needed to send continuously messages on random topics to
a broker. mqtt-randompub contains options to send a single message,
a specific count of messages, or a constant flow of messages till
the tool is terminated. Configuration files can be used to store
lists of topics to create repeatable test scenarios.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{_bindir}/mqtt-randompub
%{python3_sitelib}/mqtt_randompub/
%{python3_sitelib}/mqtt_randompub-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora