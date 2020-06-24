# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate procs

Name:           rust-%{crate}
Version:        0.10.3
Release:        2%{?dist}
Summary:        Modern replacement for ps

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/procs
Source:         %{crates_source}
# Initial patched metadata
# * No windows/macos
# * Remove docker feature
# * Update users to 0.10, https://github.com/dalance/procs/pull/61
Patch0:         procs-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Modern replacement for ps.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# * ASL 2.0
# * ASL 2.0 or MIT
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
# * zlib
License:        MIT and ASL 2.0 and zlib

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/procs

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
%cargo_test
%endif

%changelog
* Fri May 22 11:35:48 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.3-2
- Update users to 0.10

* Mon May 11 2020 Josh Stone <jistone@redhat.com> - 0.10.3-1
- Update to 0.10.3

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Sun Mar 15 09:09:36 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.20-1
- Update to 0.9.20

* Mon Mar 02 17:17:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.16-1
- Update to 0.9.16

* Tue Feb 25 08:10:30 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Tue Feb 18 13:11:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.11-1
- Initial package