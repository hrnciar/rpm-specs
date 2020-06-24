# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate hyperfine

Name:           rust-%{crate}
Version:        1.10.0
Release:        2%{?dist}
Summary:        Command-line benchmarking tool

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/hyperfine
Source:         %{crates_source}
# Initial patched metadata
# * No windows
# * Update indicatif to 0.15, https://github.com/sharkdp/hyperfine/pull/299
Patch0:         hyperfine-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Command-line benchmarking tool.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# ASL 2.0 or Boost
# MIT
# MIT or ASL 2.0
# MPLv2.0
# Unlicense or MIT
License:        ASL 2.0 and MIT and MPLv2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{_bindir}/hyperfine
%{_mandir}/man1/hyperfine.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/hyperfine.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/hyperfine.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_hyperfine

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  doc/hyperfine.1
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  target/release/build/%{crate}-*/out/hyperfine.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  target/release/build/%{crate}-*/out/hyperfine.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  target/release/build/%{crate}-*/out/_hyperfine

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jun 18 07:34:32 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.10.0-2
- Update indicatif to 0.15

* Mon May 25 17:04:54 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Wed Feb 26 2020 Josh Stone <jistone@redhat.com> - 1.9.0-4
- Bump indicatif to 0.14

* Sun Feb 16 14:38:46 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.9.0-3
- Fixup license

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:31:47 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 08:58:51 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-2
- Regenerate

* Sun Jun 09 13:46:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-3
- Bump statistical to 1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Initial package
