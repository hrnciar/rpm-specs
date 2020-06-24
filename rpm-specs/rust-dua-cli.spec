# Generated by rust2rpm 15
# * The test code is not shipped, but even if it would - the testing parts
#   are missing too.
%bcond_with check

%global crate dua-cli

Name:           rust-%{crate}
Version:        2.6.1
Release:        1%{?dist}
Summary:        Tool to conveniently learn about the disk usage of directories

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dua-cli
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Tool to conveniently learn about the disk usage of directories, fast!.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# (MIT or ASL 2.0) and BSD
# MIT
# MIT or ASL 2.0
License:        MIT and BSD

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/dua
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/Byron/dua-cli/issues/39
%cargo_test -- --   --skip interactive::app_test::journeys_with_writes::basic_user_journey_with_deletion                \
                    --skip interactive::app_test::journeys_readonly::simple_user_journey_read_only                      \
                    --skip interactive::app_test::unit::it_can_handle_ending_traversal_without_reaching_the_top         \
                    --skip interactive::app_test::unit::it_can_handle_ending_traversal_reaching_top_but_skipping_levels
%endif

%changelog
* Sun May 31 13:57:22 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Sun May 10 14:35:34 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Mon Mar 30 08:19:56 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Fri Mar 27 15:15:21 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.9-1
- Update to 2.3.9

* Thu Mar 26 08:32:46 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8

* Tue Mar 17 16:47:38 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.6-1
- Update to 2.3.6

* Sun Mar 15 18:07:16 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5

* Sun Mar 15 09:14:52 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Tue Feb 25 02:05:44 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Mon Feb 24 20:18:39 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.1-1
- Initial package
