%define octpkg vibes

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Integrates the VIBes API into Octave
Name:		octave-%{octpkg}
Version:	0.2.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and MIT
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The VIBes API allows one to easily display results (boxes, pavings) from
interval methods.
 
 annotating and exporting figures, and (2) the VIBes API that enables your
 program to communicate with the viewer in order to draw figures.
 
This package integrates the VIBes API into Octave. The VIBes application
is required for operation and must be installed seperately. Data types from
third-party interval arithmetic libraries for Octave are also supported.

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

