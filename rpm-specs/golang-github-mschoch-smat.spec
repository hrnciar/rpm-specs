# Generated by go2rpm
%bcond_without check

# https://github.com/mschoch/smat
%global goipath         github.com/mschoch/smat
%global commit          90eadee771aeab36e8bf796039b8c261bebebe4f

%gometa

%global common_description %{expand:
The concept is simple, describe valid uses of your library as states and
actions. States describe which actions are possible, and with what probability
they should occur. Actions mutate the context and transition to another state.

By doing this, two things are possible:
 - Use go-fuzz to find/test interesting sequences of operations on your library.
 - Automate longevity testing of your application by performing long sequences
   of valid operations.

Both of these can also incorporate validation logic (not just failure detection
by building validation into the state machine).}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        State Machine Assisted Testing

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/boltdb/bolt)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 18:41:22 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190306git90eadee
- Update to new macros

* Sun Mar 03 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190306git90eadee
- First package for Fedora