# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate desed

Name:           rust-%{crate}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Sed script debugger

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+

URL:            https://crates.io/crates/desed
Source:         %{crates_source}

# cargo_generate_buildrequires generates BRs for all dependencies,
# including non-Linux OS-specific ones.
# This patch removes those from Cargo.toml.
Patch0:         desed--remove-nonlinux-deps-from-cargo.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Sed script debugger. Debug and demystify your sed scripts with TUI debugger.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# * ASL 2.0 or MIT
# * MIT
# * MIT or ASL 2.0
License:        GPLv3+ and MIT
Requires:       sed >= 4.6

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/desed

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
* Mon Oct 05 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.0-1
- Update to latest release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Artur Iwicki <fedora@svgames.pl> - 1.1.4-4
- Put a minimum version requirement on sed

* Fri May 15 12:37:32 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.4-3
- Regenerate with rust2rpm

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 1.1.4-2
- Add a Requires: on sed
- Fix the license tag (GPLv3 -> GPLv3+)

* Wed May 06 2020 Artur Iwicki <fedora@svgames.pl> - 1.1.4-1
- Initial packaging
