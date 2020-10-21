%global _description %{expand:
MOD2C is NMODL to C adapted for CoreNEURON simulator.
}

# Using a snapshot: upstream does not tag releases
%global commit 5a7f820748a0ff8443dc7bdabfb371f2a042d053
%global checkoutdate 20201009

Name:       mod2c
Version:    2.1.0
Release:    1.%{checkoutdate}git%{commit}%{?dist}
Summary:    NMODL to C adapted for CoreNEURON simulator

License:    BSD
URL:        https://github.com/BlueBrain/mod2c
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  bison bison-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)

%description %_description

%prep
%autosetup -n %{name}-%{commit}

%build
%cmake -DUNIT_TESTS=ON -DFUNCTIONAL_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md CREDIT.txt
%{_bindir}/mod2c_core
%{_datadir}/nrnunits.lib

%changelog
* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-1.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Initial build
